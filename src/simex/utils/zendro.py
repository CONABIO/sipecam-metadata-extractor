import os
import requests

from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint

from simex.sipecam_zendro_schema import sipecam_zendro_schema
from simex.settings import SIPECAM_ZENDRO_GQL_URL, SIPECAM_ZENDRO_GQL_USER, \
SIPECAM_ZENDRO_GQL_PASSWORD

def get_credentials():
    return {
            "username": SIPECAM_ZENDRO_GQL_USER,
            "password": SIPECAM_ZENDRO_GQL_PASSWORD,
           }
def get_zendro_url_for_login():
    return os.path.join(SIPECAM_ZENDRO_GQL_URL,"login")

def get_zendro_url_for_gql():
    return os.path.join(SIPECAM_ZENDRO_GQL_URL, "graphql")

def get_token():
    """
    Get a token that allows to make zendro queries.

    Returns:
        token (str):  token.
    """
    login = requests.post(get_zendro_url_for_login(),
                          data=get_credentials())

    if login.status_code == 200:
        return login.json()['token']
    else:
        print("bad credentials in .simex_env")
        return None
def get_sgqlc_endpoint_and_operation_for_query():
    token = get_token()

    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
        'Content-Type': 'application/json; charset=utf-8'
    }

    endpoint = HTTPEndpoint(get_zendro_url_for_gql(),
                            headers)
    return (endpoint,
            Operation(sipecam_zendro_schema.Query))

def auxiliar_func_for_query_move_using_file_type(op,
                                                 serial_number,
                                                 file_type):
    """
    Make query using serial number of device. Helper for move_files_to_standard_directory
    """
    dict_for_physical_devices = {"field": "",
                                 "value": serial_number,
                                 "operator": "like"}
    if file_type == "image" or file_type == "video":
        dict_for_physical_devices["field"] = "serial_number"
    else:
        if file_type == "audio":
            dict_for_physical_devices["field"] = "comments"
            dict_for_physical_devices["value"] = "ADM" + dict_for_physical_devices["value"]
    op.physical_devices(pagination={"limit": 0},
                        search=dict_for_physical_devices)


def query_for_move_files_to_standard_directory(serial_number,
                                               first_date,
                                               second_date,
                                               file_type):
    """
    Execute in GQL of Zendro:
    query {
      physical_devices(pagination: {limit: 0},
                       search: {field: serial_number,
                                value: "<serial_number>",
                                operator: like})
                        {
                        device_deploymentsFilter(pagination: {limit: 0},
                                                 search: {operator: and,
                                                          search: [{field: date_deployment,
                                                                    value: "<first_date>",
                                                                    valueType: String,
                                                                    operator: gte},
                                                                  {field: date_deployment,
                                                                   value: "<second_date>",
                                                                   valueType: String,
                                                                   operator: lte}]
                                                          })
                                                 {
                                                  node {
                                                      nomenclatura
                                                      cat_integr
                                                      ecosystems{
                                                          name
                                                                }
                                                       }
                                                  cumulus {
                                                      geometry
                                                      name
                                                       }
                                                  date_deployment
                                                  latitude
                                                  longitude
                                                  }
                        }
          }
    """
    endpoint, op = get_sgqlc_endpoint_and_operation_for_query()
    auxiliar_func_for_query_move_using_file_type(op, serial_number, file_type)

    dict_for_device_deployments_filter_1 = {"field"   : "date_deployment",
                                            "value"   : first_date,
                                            "valueType": "String",
                                            "operator": "gte"}
    dict_for_device_deployments_filter_2 = {"field"   : "date_deployment",
                                            "value"   : second_date,
                                            "valueType": "String",
                                            "operator": "lte"}
    list_for_device_deployments_filter = [dict_for_device_deployments_filter_1,
                                          dict_for_device_deployments_filter_2]

    op.physical_devices.device_deployments_filter(pagination={"limit": 0},
                                                  search={"operator": "and",
                                                          "search": list_for_device_deployments_filter
                                                          }
                                                  )
    op.physical_devices.device_deployments_filter.node.nomenclatura() #after this line op has type sgqlc selection
    op.physical_devices.device_deployments_filter.node.cat_integr()
    op.physical_devices.device_deployments_filter.node.ecosystems.name()
    op.physical_devices.device_deployments_filter.cumulus.name()
    op.physical_devices.device_deployments_filter.cumulus.geometry()
    op.physical_devices.device_deployments_filter.date_deployment()
    op.physical_devices.device_deployments_filter.latitude()
    op.physical_devices.device_deployments_filter.longitude()
    query_result = endpoint(op)
    return (query_result, op)

def query_alternative_auxiliar_for_move_files_to_standard_directory(serial_number,
                                                                    file_type):
    """
    Execute in GQL of Zendro:
    query {
      physical_devices(pagination: {limit: 0},
                       search: {field: serial_number,
                       value: "<serial_number>",
                       operator: like})
                       {
                        device_deploymentsFilter(pagination: {limit: 0})
                                                 {
                                                   date_deployment
                                                 }
                       }
    }
    """
    endpoint, op = get_sgqlc_endpoint_and_operation_for_query()
    auxiliar_func_for_query_move_using_file_type(op, serial_number, file_type)
    op.physical_devices.device_deployments_filter(pagination={"limit": 0}).date_deployment()
    query_result = endpoint(op)
    return (query_result, op)

def query_alternative_for_move_files_to_standard_directory(serial_number,
                                                           date_for_filter,
                                                           file_type):
    """
    Execute in GQL of Zendro:
    query {
      physical_devices(pagination: {limit: 0},
                       search: {field: serial_number,
                                value: "<serial_number>",
                                operator: like})
                       {
                        device_deploymentsFilter(pagination: {limit: 0},
                                                 search: {field: date_deployment,
                                                 value: "<date_for_filter>",
                                                 operator: eq})
                                                 {
                                                  node {
                                                      nomenclatura
                                                      cat_integr
                                                      ecosystems{
                                                          name
                                                                }
                                                       }
                                                  cumulus {
                                                      geometry
                                                      name
                                                       }
                                                  date_deployment
                                                  latitude
                                                  longitude
                                                  }
                       }
    }
    """
    endpoint, op = get_sgqlc_endpoint_and_operation_for_query()
    auxiliar_func_for_query_move_using_file_type(op, serial_number, file_type)
    op.physical_devices.device_deployments_filter(pagination={"limit": 0},
                                                  search={"field": "date_deployment",
                                                          "value": date_for_filter,
                                                          "operator": "eq"})
    op.physical_devices.device_deployments_filter.node.nomenclatura() #after this line op has type sgqlc selection
    op.physical_devices.device_deployments_filter.node.cat_integr()
    op.physical_devices.device_deployments_filter.node.ecosystems.name()
    op.physical_devices.device_deployments_filter.cumulus.name()
    op.physical_devices.device_deployments_filter.cumulus.geometry()
    op.physical_devices.device_deployments_filter.date_deployment()
    op.physical_devices.device_deployments_filter.latitude()
    op.physical_devices.device_deployments_filter.longitude()
    query_result = endpoint(op)
    return (query_result, op)

def query_for_extend_metadata_of_files(serial_number,
                                       first_date,
                                       second_date,
                                       file_type):
    """
    Execute in GQL of Zendro:
    query {
      physical_devices(pagination: {limit: 0},
                       search: {field: serial_number,
                                value: "<serial_number>",
                                operator: like})
                        {
                        device_deploymentsFilter(pagination: {limit: 0},
                                                 search: {operator: and,
                                                          search: [{field: date_deployment,
                                                                    value: "<first_date>",
                                                                    valueType: String,
                                                                    operator: gte},
                                                                  {field: date_deployment,
                                                                   value: "<second_date>",
                                                                   valueType: String,
                                                                   operator: lte}]
                                                          })
                                                 {
                                                  cumulus {
                                                      geometry
                                                       }
                                                  }
                        }
          }
    """
    endpoint, op = get_sgqlc_endpoint_and_operation_for_query()
    auxiliar_func_for_query_move_using_file_type(op, serial_number, file_type)

    dict_for_device_deployments_filter_1 = {"field"   : "date_deployment",
                                            "value"   : first_date,
                                            "valueType": "String",
                                            "operator": "gte"}
    dict_for_device_deployments_filter_2 = {"field"   : "date_deployment",
                                            "value"   : second_date,
                                            "valueType": "String",
                                            "operator": "lte"}
    list_for_device_deployments_filter = [dict_for_device_deployments_filter_1,
                                          dict_for_device_deployments_filter_2]

    op.physical_devices.device_deployments_filter(pagination={"limit": 0},
                                                  search={"operator": "and",
                                                          "search": list_for_device_deployments_filter
                                                          }
                                                  )
    op.physical_devices.device_deployments_filter.cumulus.geometry() #after this line op has type sgqlc selection
    query_result = endpoint(op)
    return (query_result, op)