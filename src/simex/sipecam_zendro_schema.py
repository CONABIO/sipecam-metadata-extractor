import sgqlc.types
import sgqlc.types.datetime


sipecam_zendro_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AmazonS3Operator(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('and', 'between', 'contains', 'eq', 'gt', 'gte', 'iLike', 'in', 'like', 'lt', 'lte', 'ne', 'not', 'notBetween', 'notContains', 'notILike', 'notIn', 'notLike', 'or')


Boolean = sgqlc.types.Boolean

class CassandraOperator(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('and', 'contains', 'eq', 'gt', 'gte', 'in', 'lt', 'lte', 'ne')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

class GenericPrestoSqlOperator(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('and', 'between', 'contains', 'eq', 'gt', 'gte', 'iLike', 'iRegexp', 'in', 'like', 'lt', 'lte', 'ne', 'not', 'notBetween', 'notContains', 'notILike', 'notIRegexp', 'notIn', 'notLike', 'notRegexp', 'or', 'regexp')


class GeoJSONFeatureCollectionScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONFeatureScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONGeometryCollectionScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONLineStringScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONMultiLineStringScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONMultiPointScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONMultiPolygonScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONPointScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GeoJSONPolygonScalar(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class GraphQLJSONObject(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


ID = sgqlc.types.ID

class InputType(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('Array', 'Boolean', 'Date', 'DateTime', 'Float', 'Int', 'String', 'Time')


Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class JSONObject(sgqlc.types.Scalar):
    __schema__ = sipecam_zendro_schema


class MongodbNeo4jOperator(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('and', 'contains', 'eq', 'gt', 'gte', 'iLike', 'iRegexp', 'in', 'like', 'lt', 'lte', 'ne', 'not', 'notContains', 'notILike', 'notIRegexp', 'notIn', 'notLike', 'notRegexp', 'or', 'regexp')


class Order(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('ASC', 'DESC')


String = sgqlc.types.String

Time = sgqlc.types.datetime.Time

class annotations_geom_obs_typeField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('classification_method', 'classified_by', 'confidence', 'createdAt', 'file_id', 'frequency_max', 'frequency_min', 'geometry', 'id', 'observation_type', 'pipeline_id', 'time_max', 'time_min', 'updatedAt', 'user_id', 'video_frame_num')


class calendarField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('date_finished', 'date_started', 'id', 'order', 'sipecam_year')


class cumulusField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('con_socio', 'criteria_id', 'ecosystem_id', 'geometry', 'id', 'name', 'user_ids')


class cumulus_criteriaField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('id', 'name')


class deploymentField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('altitude', 'comments', 'cumulus_id', 'date_deployment', 'device_id', 'id', 'kobo_url', 'latitude', 'longitude', 'metadata', 'node_id')


class device_catalogField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('brand', 'id', 'type')


class ecosystemField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('id', 'name')


class fileField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('createdAt', 'date_deployment_device', 'deployment_id', 'id', 'id_alfresco', 'storage', 'type', 'updatedAt', 'url')


class file_countField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('audio_files', 'cumulus_id', 'delivery_date', 'id', 'image_files', 'size', 'video_files')


class individualField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('altitude', 'arete', 'clave_posicion_malla', 'comments', 'cumulus_id', 'date_trap', 'id', 'kobo_url', 'latitude', 'longitude', 'metadata', 'node_id')


class institutionField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('address', 'id', 'name', 'phone_number')


class monitorField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('contact', 'cumulus_id', 'first_name', 'id', 'last_name', 'second_last_name', 'visit_ids')


class nodeField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('cat_integr', 'con_socio', 'cumulus_id', 'ecosystem_id', 'fid', 'id', 'location', 'nomenclatura')


class physical_deviceField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('comments', 'cumulus_id', 'device_id', 'id', 'previous_cumulus_ids', 'serial_number', 'status')


class pipeline_infoField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('comments', 'commit_dvc_of_data_ref', 'createdAt', 'id', 'updatedAt', 'url_repo_model', 'version')


class productField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('comments', 'createdAt', 'file_id', 'id', 'metadata', 'observation_type', 'pipeline_id', 'producer', 'project', 'type', 'updatedAt', 'url')


class roleField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('description', 'id', 'name')


class role_to_userField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('id', 'role_id', 'user_id')


class transectField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('date_transecto', 'id', 'latitude', 'longitude', 'node_id', 'number', 'percentage', 'sum_impact', 'sum_indicator_species', 'sum_vegetation_structure')


class userField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('cumulus_ids', 'email', 'first_name', 'id', 'institution_id', 'is_active', 'last_login', 'last_name', 'password', 'username')


class visitField(sgqlc.types.Enum):
    __schema__ = sipecam_zendro_schema
    __choices__ = ('comments', 'cumulus_id', 'date_first_season', 'date_second_season', 'date_sipecam_first_season', 'date_sipecam_second_season', 'disturbed_id', 'id', 'monitor_ids', 'pristine_id', 'report_first_season', 'report_second_season')



########################################################################
# Input Objects
########################################################################
class bulkAssociationAnnotations_geom_obs_typeWithFile_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'file_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    file_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='file_id')


class bulkAssociationAnnotations_geom_obs_typeWithPipeline_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'pipeline_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipeline_id')


class bulkAssociationAnnotations_geom_obs_typeWithUser_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'user_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='user_id')


class bulkAssociationCumulusWithCriteria_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'criteria_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    criteria_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='criteria_id')


class bulkAssociationCumulusWithEcosystem_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'ecosystem_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ecosystem_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ecosystem_id')


class bulkAssociationDeploymentWithCumulus_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'cumulus_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cumulus_id')


class bulkAssociationDeploymentWithDevice_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'device_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    device_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='device_id')


class bulkAssociationDeploymentWithNode_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'node_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='node_id')


class bulkAssociationFileWithDeployment_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'deployment_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    deployment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='deployment_id')


class bulkAssociationFile_countWithCumulus_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'cumulus_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cumulus_id')


class bulkAssociationIndividualWithCumulus_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'cumulus_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cumulus_id')


class bulkAssociationIndividualWithNode_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'node_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='node_id')


class bulkAssociationMonitorWithCumulus_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'cumulus_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cumulus_id')


class bulkAssociationNodeWithCumulus_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'cumulus_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cumulus_id')


class bulkAssociationNodeWithEcosystem_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'ecosystem_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ecosystem_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ecosystem_id')


class bulkAssociationPhysical_deviceWithCumulus_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'cumulus_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cumulus_id')


class bulkAssociationPhysical_deviceWithDevice_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'device_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    device_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='device_id')


class bulkAssociationProductWithFile_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'file_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    file_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='file_id')


class bulkAssociationProductWithPipeline_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'pipeline_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipeline_id')


class bulkAssociationTransectWithNode_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'node_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='node_id')


class bulkAssociationUserWithInstitution_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'institution_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    institution_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='institution_id')


class bulkAssociationVisitWithCumulus_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'cumulus_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cumulus_id')


class bulkAssociationVisitWithDisturbed_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'disturbed_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    disturbed_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='disturbed_id')


class bulkAssociationVisitWithPristine_idInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'pristine_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pristine_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pristine_id')


class orderAnnotations_geom_obs_typeInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(annotations_geom_obs_typeField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderCalendarInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(calendarField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderCumulusInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(cumulusField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderCumulus_criteriaInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(cumulus_criteriaField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderDeploymentInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(deploymentField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderDevice_catalogInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(device_catalogField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderEcosystemInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(ecosystemField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderFileInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(fileField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderFile_countInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(file_countField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderIndividualInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(individualField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderInstitutionInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(institutionField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderMonitorInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(monitorField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderNodeInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(nodeField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderPhysical_deviceInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(physical_deviceField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderPipeline_infoInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(pipeline_infoField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderProductInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(productField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderRoleInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(roleField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderRole_to_userInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(role_to_userField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderTransectInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(transectField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderUserInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(userField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class orderVisitInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(visitField, graphql_name='field')
    order = sgqlc.types.Field(Order, graphql_name='order')


class paginationCursorInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('first', 'last', 'after', 'before', 'include_cursor')
    first = sgqlc.types.Field(Int, graphql_name='first')
    last = sgqlc.types.Field(Int, graphql_name='last')
    after = sgqlc.types.Field(String, graphql_name='after')
    before = sgqlc.types.Field(String, graphql_name='before')
    include_cursor = sgqlc.types.Field(Boolean, graphql_name='includeCursor')


class paginationInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('limit', 'offset')
    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='limit')
    offset = sgqlc.types.Field(Int, graphql_name='offset')


class searchAnnotations_geom_obs_typeInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(annotations_geom_obs_typeField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchAnnotations_geom_obs_typeInput'), graphql_name='search')


class searchCalendarInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(calendarField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchCalendarInput'), graphql_name='search')


class searchCumulusInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(cumulusField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchCumulusInput'), graphql_name='search')


class searchCumulus_criteriaInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(cumulus_criteriaField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchCumulus_criteriaInput'), graphql_name='search')


class searchDeploymentInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(deploymentField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchDeploymentInput'), graphql_name='search')


class searchDevice_catalogInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(device_catalogField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchDevice_catalogInput'), graphql_name='search')


class searchEcosystemInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(ecosystemField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchEcosystemInput'), graphql_name='search')


class searchFileInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(fileField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchFileInput'), graphql_name='search')


class searchFile_countInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(file_countField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchFile_countInput'), graphql_name='search')


class searchIndividualInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(individualField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchIndividualInput'), graphql_name='search')


class searchInstitutionInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(institutionField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchInstitutionInput'), graphql_name='search')


class searchMonitorInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(monitorField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchMonitorInput'), graphql_name='search')


class searchNodeInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(nodeField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchNodeInput'), graphql_name='search')


class searchPhysical_deviceInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(physical_deviceField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchPhysical_deviceInput'), graphql_name='search')


class searchPipeline_infoInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(pipeline_infoField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchPipeline_infoInput'), graphql_name='search')


class searchProductInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(productField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchProductInput'), graphql_name='search')


class searchRoleInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(roleField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchRoleInput'), graphql_name='search')


class searchRole_to_userInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(role_to_userField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchRole_to_userInput'), graphql_name='search')


class searchTransectInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(transectField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchTransectInput'), graphql_name='search')


class searchUserInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(userField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchUserInput'), graphql_name='search')


class searchVisitInput(sgqlc.types.Input):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('field', 'value', 'value_type', 'operator', 'search')
    field = sgqlc.types.Field(visitField, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(InputType, graphql_name='valueType')
    operator = sgqlc.types.Field(GenericPrestoSqlOperator, graphql_name='operator')
    search = sgqlc.types.Field(sgqlc.types.list_of('searchVisitInput'), graphql_name='search')



########################################################################
# Output Objects and Interfaces
########################################################################
class Annotations_geom_obs_typeConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'annotations_geom_obs_types', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('Annotations_geom_obs_typeEdge'), graphql_name='edges')
    annotations_geom_obs_types = sgqlc.types.Field(sgqlc.types.list_of('annotations_geom_obs_type'), graphql_name='annotations_geom_obs_types')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class Annotations_geom_obs_typeEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('annotations_geom_obs_type'), graphql_name='node')


class CalendarConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'calendars', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CalendarEdge'), graphql_name='edges')
    calendars = sgqlc.types.Field(sgqlc.types.list_of('calendar'), graphql_name='calendars')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class CalendarEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('calendar'), graphql_name='node')


class CumulusConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'cumulus', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CumulusEdge'), graphql_name='edges')
    cumulus = sgqlc.types.Field(sgqlc.types.list_of('cumulus'), graphql_name='cumulus')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class CumulusEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('cumulus'), graphql_name='node')


class Cumulus_criteriaConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'cumulus_criteria', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('Cumulus_criteriaEdge'), graphql_name='edges')
    cumulus_criteria = sgqlc.types.Field(sgqlc.types.list_of('cumulus_criteria'), graphql_name='cumulus_criteria')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class Cumulus_criteriaEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('cumulus_criteria'), graphql_name='node')


class DeploymentConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'deployments', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentEdge'), graphql_name='edges')
    deployments = sgqlc.types.Field(sgqlc.types.list_of('deployment'), graphql_name='deployments')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class DeploymentEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('deployment'), graphql_name='node')


class Device_catalogConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'device_catalogs', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('Device_catalogEdge'), graphql_name='edges')
    device_catalogs = sgqlc.types.Field(sgqlc.types.list_of('device_catalog'), graphql_name='device_catalogs')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class Device_catalogEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('device_catalog'), graphql_name='node')


class EcosystemConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'ecosystems', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EcosystemEdge'), graphql_name='edges')
    ecosystems = sgqlc.types.Field(sgqlc.types.list_of('ecosystem'), graphql_name='ecosystems')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class EcosystemEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ecosystem'), graphql_name='node')


class FileConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'files', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('FileEdge'), graphql_name='edges')
    files = sgqlc.types.Field(sgqlc.types.list_of('file'), graphql_name='files')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class FileEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('file'), graphql_name='node')


class File_countConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'file_counts', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('File_countEdge'), graphql_name='edges')
    file_counts = sgqlc.types.Field(sgqlc.types.list_of('file_count'), graphql_name='file_counts')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class File_countEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('file_count'), graphql_name='node')


class IndividualConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'individuals', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('IndividualEdge'), graphql_name='edges')
    individuals = sgqlc.types.Field(sgqlc.types.list_of('individual'), graphql_name='individuals')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class IndividualEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('individual'), graphql_name='node')


class InstitutionConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'institutions', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('InstitutionEdge'), graphql_name='edges')
    institutions = sgqlc.types.Field(sgqlc.types.list_of('institution'), graphql_name='institutions')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class InstitutionEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('institution'), graphql_name='node')


class MonitorConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'monitors', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('MonitorEdge'), graphql_name='edges')
    monitors = sgqlc.types.Field(sgqlc.types.list_of('monitor'), graphql_name='monitors')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class MonitorEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('monitor'), graphql_name='node')


class Mutation(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('add_annotations_geom_obs_type', 'update_annotations_geom_obs_type', 'delete_annotations_geom_obs_type', 'bulk_associate_annotations_geom_obs_type_with_file_id', 'bulk_dis_associate_annotations_geom_obs_type_with_file_id', 'bulk_associate_annotations_geom_obs_type_with_user_id', 'bulk_dis_associate_annotations_geom_obs_type_with_user_id', 'bulk_associate_annotations_geom_obs_type_with_pipeline_id', 'bulk_dis_associate_annotations_geom_obs_type_with_pipeline_id', 'add_calendar', 'update_calendar', 'delete_calendar', 'add_cumulus', 'update_cumulus', 'delete_cumulus', 'bulk_associate_cumulus_with_criteria_id', 'bulk_dis_associate_cumulus_with_criteria_id', 'bulk_associate_cumulus_with_ecosystem_id', 'bulk_dis_associate_cumulus_with_ecosystem_id', 'add_cumulus_criteria', 'update_cumulus_criteria', 'delete_cumulus_criteria', 'add_deployment', 'update_deployment', 'delete_deployment', 'bulk_associate_deployment_with_device_id', 'bulk_dis_associate_deployment_with_device_id', 'bulk_associate_deployment_with_node_id', 'bulk_dis_associate_deployment_with_node_id', 'bulk_associate_deployment_with_cumulus_id', 'bulk_dis_associate_deployment_with_cumulus_id', 'add_device_catalog', 'update_device_catalog', 'delete_device_catalog', 'add_ecosystem', 'update_ecosystem', 'delete_ecosystem', 'add_file', 'update_file', 'delete_file', 'bulk_associate_file_with_deployment_id', 'bulk_dis_associate_file_with_deployment_id', 'add_file_count', 'update_file_count', 'delete_file_count', 'bulk_associate_file_count_with_cumulus_id', 'bulk_dis_associate_file_count_with_cumulus_id', 'add_individual', 'update_individual', 'delete_individual', 'bulk_associate_individual_with_node_id', 'bulk_dis_associate_individual_with_node_id', 'bulk_associate_individual_with_cumulus_id', 'bulk_dis_associate_individual_with_cumulus_id', 'add_institution', 'update_institution', 'delete_institution', 'add_monitor', 'update_monitor', 'delete_monitor', 'bulk_associate_monitor_with_cumulus_id', 'bulk_dis_associate_monitor_with_cumulus_id', 'add_node', 'update_node', 'delete_node', 'bulk_associate_node_with_cumulus_id', 'bulk_dis_associate_node_with_cumulus_id', 'bulk_associate_node_with_ecosystem_id', 'bulk_dis_associate_node_with_ecosystem_id', 'add_physical_device', 'update_physical_device', 'delete_physical_device', 'bulk_associate_physical_device_with_device_id', 'bulk_dis_associate_physical_device_with_device_id', 'bulk_associate_physical_device_with_cumulus_id', 'bulk_dis_associate_physical_device_with_cumulus_id', 'add_pipeline_info', 'update_pipeline_info', 'delete_pipeline_info', 'add_product', 'update_product', 'delete_product', 'bulk_associate_product_with_file_id', 'bulk_dis_associate_product_with_file_id', 'bulk_associate_product_with_pipeline_id', 'bulk_dis_associate_product_with_pipeline_id', 'add_role', 'update_role', 'delete_role', 'add_role_to_user', 'update_role_to_user', 'delete_role_to_user', 'add_transect', 'update_transect', 'delete_transect', 'bulk_associate_transect_with_node_id', 'bulk_dis_associate_transect_with_node_id', 'add_user', 'update_user', 'delete_user', 'bulk_associate_user_with_institution_id', 'bulk_dis_associate_user_with_institution_id', 'add_visit', 'update_visit', 'delete_visit', 'bulk_associate_visit_with_cumulus_id', 'bulk_dis_associate_visit_with_cumulus_id', 'bulk_associate_visit_with_pristine_id', 'bulk_dis_associate_visit_with_pristine_id', 'bulk_associate_visit_with_disturbed_id', 'bulk_dis_associate_visit_with_disturbed_id')
    add_annotations_geom_obs_type = sgqlc.types.Field(sgqlc.types.non_null('annotations_geom_obs_type'), graphql_name='addAnnotations_geom_obs_type', args=sgqlc.types.ArgDict((
        ('classified_by', sgqlc.types.Arg(String, graphql_name='classified_by', default=None)),
        ('classification_method', sgqlc.types.Arg(String, graphql_name='classification_method', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('confidence', sgqlc.types.Arg(Float, graphql_name='confidence', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONGeometryCollectionScalar, graphql_name='geometry', default=None)),
        ('video_frame_num', sgqlc.types.Arg(Int, graphql_name='video_frame_num', default=None)),
        ('frequency_min', sgqlc.types.Arg(Float, graphql_name='frequency_min', default=None)),
        ('frequency_max', sgqlc.types.Arg(Float, graphql_name='frequency_max', default=None)),
        ('time_min', sgqlc.types.Arg(Float, graphql_name='time_min', default=None)),
        ('time_max', sgqlc.types.Arg(Float, graphql_name='time_max', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_file_to', sgqlc.types.Arg(ID, graphql_name='addFileTo', default=None)),
        ('add_user_to', sgqlc.types.Arg(ID, graphql_name='addUserTo', default=None)),
        ('add_pipeline_annotation', sgqlc.types.Arg(ID, graphql_name='addPipeline_annotation', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_annotations_geom_obs_type = sgqlc.types.Field(sgqlc.types.non_null('annotations_geom_obs_type'), graphql_name='updateAnnotations_geom_obs_type', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('classified_by', sgqlc.types.Arg(String, graphql_name='classified_by', default=None)),
        ('classification_method', sgqlc.types.Arg(String, graphql_name='classification_method', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('confidence', sgqlc.types.Arg(Float, graphql_name='confidence', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONGeometryCollectionScalar, graphql_name='geometry', default=None)),
        ('video_frame_num', sgqlc.types.Arg(Int, graphql_name='video_frame_num', default=None)),
        ('frequency_min', sgqlc.types.Arg(Float, graphql_name='frequency_min', default=None)),
        ('frequency_max', sgqlc.types.Arg(Float, graphql_name='frequency_max', default=None)),
        ('time_min', sgqlc.types.Arg(Float, graphql_name='time_min', default=None)),
        ('time_max', sgqlc.types.Arg(Float, graphql_name='time_max', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_file_to', sgqlc.types.Arg(ID, graphql_name='addFileTo', default=None)),
        ('remove_file_to', sgqlc.types.Arg(ID, graphql_name='removeFileTo', default=None)),
        ('add_user_to', sgqlc.types.Arg(ID, graphql_name='addUserTo', default=None)),
        ('remove_user_to', sgqlc.types.Arg(ID, graphql_name='removeUserTo', default=None)),
        ('add_pipeline_annotation', sgqlc.types.Arg(ID, graphql_name='addPipeline_annotation', default=None)),
        ('remove_pipeline_annotation', sgqlc.types.Arg(ID, graphql_name='removePipeline_annotation', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_annotations_geom_obs_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteAnnotations_geom_obs_type', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_annotations_geom_obs_type_with_file_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateAnnotations_geom_obs_typeWithFile_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationAnnotations_geom_obs_typeWithFile_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_annotations_geom_obs_type_with_file_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateAnnotations_geom_obs_typeWithFile_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationAnnotations_geom_obs_typeWithFile_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_annotations_geom_obs_type_with_user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateAnnotations_geom_obs_typeWithUser_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationAnnotations_geom_obs_typeWithUser_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_annotations_geom_obs_type_with_user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateAnnotations_geom_obs_typeWithUser_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationAnnotations_geom_obs_typeWithUser_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_annotations_geom_obs_type_with_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateAnnotations_geom_obs_typeWithPipeline_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationAnnotations_geom_obs_typeWithPipeline_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_annotations_geom_obs_type_with_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateAnnotations_geom_obs_typeWithPipeline_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationAnnotations_geom_obs_typeWithPipeline_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_calendar = sgqlc.types.Field(sgqlc.types.non_null('calendar'), graphql_name='addCalendar', args=sgqlc.types.ArgDict((
        ('date_started', sgqlc.types.Arg(Date, graphql_name='date_started', default=None)),
        ('date_finished', sgqlc.types.Arg(Date, graphql_name='date_finished', default=None)),
        ('sipecam_year', sgqlc.types.Arg(String, graphql_name='sipecam_year', default=None)),
        ('order', sgqlc.types.Arg(Int, graphql_name='order', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_calendar = sgqlc.types.Field(sgqlc.types.non_null('calendar'), graphql_name='updateCalendar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date_started', sgqlc.types.Arg(Date, graphql_name='date_started', default=None)),
        ('date_finished', sgqlc.types.Arg(Date, graphql_name='date_finished', default=None)),
        ('sipecam_year', sgqlc.types.Arg(String, graphql_name='sipecam_year', default=None)),
        ('order', sgqlc.types.Arg(Int, graphql_name='order', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_calendar = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteCalendar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_cumulus = sgqlc.types.Field(sgqlc.types.non_null('cumulus'), graphql_name='addCumulus', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONPolygonScalar, graphql_name='geometry', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('add_cumulus_criteria', sgqlc.types.Arg(ID, graphql_name='addCumulus_criteria', default=None)),
        ('add_unique_ecosystem', sgqlc.types.Arg(ID, graphql_name='addUnique_ecosystem', default=None)),
        ('add_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevices', default=None)),
        ('add_associated_partners', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_partners', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('add_nodes', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addNodes', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('add_file_counts', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_counts', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_cumulus = sgqlc.types.Field(sgqlc.types.non_null('cumulus'), graphql_name='updateCumulus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONPolygonScalar, graphql_name='geometry', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('add_cumulus_criteria', sgqlc.types.Arg(ID, graphql_name='addCumulus_criteria', default=None)),
        ('remove_cumulus_criteria', sgqlc.types.Arg(ID, graphql_name='removeCumulus_criteria', default=None)),
        ('add_unique_ecosystem', sgqlc.types.Arg(ID, graphql_name='addUnique_ecosystem', default=None)),
        ('remove_unique_ecosystem', sgqlc.types.Arg(ID, graphql_name='removeUnique_ecosystem', default=None)),
        ('add_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevices', default=None)),
        ('remove_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDevices', default=None)),
        ('add_associated_partners', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_partners', default=None)),
        ('remove_associated_partners', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeAssociated_partners', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('remove_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeVisits', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('remove_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeMonitors', default=None)),
        ('add_nodes', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addNodes', default=None)),
        ('remove_nodes', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeNodes', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('remove_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('remove_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeIndividuals', default=None)),
        ('add_file_counts', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_counts', default=None)),
        ('remove_file_counts', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFile_counts', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_cumulus = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteCumulus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_cumulus_with_criteria_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateCumulusWithCriteria_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationCumulusWithCriteria_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_cumulus_with_criteria_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateCumulusWithCriteria_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationCumulusWithCriteria_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_cumulus_with_ecosystem_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateCumulusWithEcosystem_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationCumulusWithEcosystem_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_cumulus_with_ecosystem_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateCumulusWithEcosystem_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationCumulusWithEcosystem_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_cumulus_criteria = sgqlc.types.Field(sgqlc.types.non_null('cumulus_criteria'), graphql_name='addCumulus_criteria', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_cumulus_criteria = sgqlc.types.Field(sgqlc.types.non_null('cumulus_criteria'), graphql_name='updateCumulus_criteria', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus', default=None)),
        ('remove_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeCumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_cumulus_criteria = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteCumulus_criteria', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_deployment = sgqlc.types.Field(sgqlc.types.non_null('deployment'), graphql_name='addDeployment', args=sgqlc.types.ArgDict((
        ('date_deployment', sgqlc.types.Arg(DateTime, graphql_name='date_deployment', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('add_node', sgqlc.types.Arg(ID, graphql_name='addNode', default=None)),
        ('add_cumulus', sgqlc.types.Arg(ID, graphql_name='addCumulus', default=None)),
        ('add_files', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFiles', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_deployment = sgqlc.types.Field(sgqlc.types.non_null('deployment'), graphql_name='updateDeployment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date_deployment', sgqlc.types.Arg(DateTime, graphql_name='date_deployment', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('remove_device', sgqlc.types.Arg(ID, graphql_name='removeDevice', default=None)),
        ('add_node', sgqlc.types.Arg(ID, graphql_name='addNode', default=None)),
        ('remove_node', sgqlc.types.Arg(ID, graphql_name='removeNode', default=None)),
        ('add_cumulus', sgqlc.types.Arg(ID, graphql_name='addCumulus', default=None)),
        ('remove_cumulus', sgqlc.types.Arg(ID, graphql_name='removeCumulus', default=None)),
        ('add_files', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFiles', default=None)),
        ('remove_files', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFiles', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_deployment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteDeployment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_deployment_with_device_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateDeploymentWithDevice_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationDeploymentWithDevice_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_deployment_with_device_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateDeploymentWithDevice_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationDeploymentWithDevice_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_deployment_with_node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateDeploymentWithNode_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationDeploymentWithNode_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_deployment_with_node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateDeploymentWithNode_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationDeploymentWithNode_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_deployment_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateDeploymentWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationDeploymentWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_deployment_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateDeploymentWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationDeploymentWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_device_catalog = sgqlc.types.Field(sgqlc.types.non_null('device_catalog'), graphql_name='addDevice_catalog', args=sgqlc.types.ArgDict((
        ('brand', sgqlc.types.Arg(String, graphql_name='brand', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('add_physical_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPhysical_devices', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_device_catalog = sgqlc.types.Field(sgqlc.types.non_null('device_catalog'), graphql_name='updateDevice_catalog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('brand', sgqlc.types.Arg(String, graphql_name='brand', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('add_physical_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPhysical_devices', default=None)),
        ('remove_physical_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removePhysical_devices', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_device_catalog = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteDevice_catalog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_ecosystem = sgqlc.types.Field(sgqlc.types.non_null('ecosystem'), graphql_name='addEcosystem', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_unique_node', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUnique_node', default=None)),
        ('add_cumulus_ecosystem', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus_ecosystem', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_ecosystem = sgqlc.types.Field(sgqlc.types.non_null('ecosystem'), graphql_name='updateEcosystem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_unique_node', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUnique_node', default=None)),
        ('remove_unique_node', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUnique_node', default=None)),
        ('add_cumulus_ecosystem', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus_ecosystem', default=None)),
        ('remove_cumulus_ecosystem', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeCumulus_ecosystem', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_ecosystem = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteEcosystem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_file = sgqlc.types.Field(sgqlc.types.non_null('file'), graphql_name='addFile', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('date_deployment_device', sgqlc.types.Arg(Date, graphql_name='date_deployment_device', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('id_alfresco', sgqlc.types.Arg(String, graphql_name='id_alfresco', default=None)),
        ('storage', sgqlc.types.Arg(String, graphql_name='storage', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_associated_deployment', sgqlc.types.Arg(ID, graphql_name='addAssociated_deployment', default=None)),
        ('add_file_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_annotations', default=None)),
        ('add_file_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_products', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_file = sgqlc.types.Field(sgqlc.types.non_null('file'), graphql_name='updateFile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('date_deployment_device', sgqlc.types.Arg(Date, graphql_name='date_deployment_device', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('id_alfresco', sgqlc.types.Arg(String, graphql_name='id_alfresco', default=None)),
        ('storage', sgqlc.types.Arg(String, graphql_name='storage', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_associated_deployment', sgqlc.types.Arg(ID, graphql_name='addAssociated_deployment', default=None)),
        ('remove_associated_deployment', sgqlc.types.Arg(ID, graphql_name='removeAssociated_deployment', default=None)),
        ('add_file_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_annotations', default=None)),
        ('remove_file_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFile_annotations', default=None)),
        ('add_file_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_products', default=None)),
        ('remove_file_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFile_products', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_file = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteFile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_file_with_deployment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateFileWithDeployment_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationFileWithDeployment_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_file_with_deployment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateFileWithDeployment_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationFileWithDeployment_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_file_count = sgqlc.types.Field(sgqlc.types.non_null('file_count'), graphql_name='addFile_count', args=sgqlc.types.ArgDict((
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='delivery_date', default=None)),
        ('audio_files', sgqlc.types.Arg(Int, graphql_name='audio_files', default=None)),
        ('image_files', sgqlc.types.Arg(Int, graphql_name='image_files', default=None)),
        ('video_files', sgqlc.types.Arg(Int, graphql_name='video_files', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
        ('add_cumulus_files', sgqlc.types.Arg(ID, graphql_name='addCumulus_files', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_file_count = sgqlc.types.Field(sgqlc.types.non_null('file_count'), graphql_name='updateFile_count', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='delivery_date', default=None)),
        ('audio_files', sgqlc.types.Arg(Int, graphql_name='audio_files', default=None)),
        ('image_files', sgqlc.types.Arg(Int, graphql_name='image_files', default=None)),
        ('video_files', sgqlc.types.Arg(Int, graphql_name='video_files', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
        ('add_cumulus_files', sgqlc.types.Arg(ID, graphql_name='addCumulus_files', default=None)),
        ('remove_cumulus_files', sgqlc.types.Arg(ID, graphql_name='removeCumulus_files', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_file_count = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteFile_count', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_file_count_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateFile_countWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationFile_countWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_file_count_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateFile_countWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationFile_countWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_individual = sgqlc.types.Field(sgqlc.types.non_null('individual'), graphql_name='addIndividual', args=sgqlc.types.ArgDict((
        ('date_trap', sgqlc.types.Arg(DateTime, graphql_name='date_trap', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('clave_posicion_malla', sgqlc.types.Arg(String, graphql_name='clave_posicion_malla', default=None)),
        ('arete', sgqlc.types.Arg(Int, graphql_name='arete', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(ID, graphql_name='addAssociated_cumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_individual = sgqlc.types.Field(sgqlc.types.non_null('individual'), graphql_name='updateIndividual', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date_trap', sgqlc.types.Arg(DateTime, graphql_name='date_trap', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('clave_posicion_malla', sgqlc.types.Arg(String, graphql_name='clave_posicion_malla', default=None)),
        ('arete', sgqlc.types.Arg(Int, graphql_name='arete', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('remove_associated_node', sgqlc.types.Arg(ID, graphql_name='removeAssociated_node', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(ID, graphql_name='addAssociated_cumulus', default=None)),
        ('remove_associated_cumulus', sgqlc.types.Arg(ID, graphql_name='removeAssociated_cumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_individual = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteIndividual', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_individual_with_node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateIndividualWithNode_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationIndividualWithNode_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_individual_with_node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateIndividualWithNode_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationIndividualWithNode_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_individual_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateIndividualWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationIndividualWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_individual_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateIndividualWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationIndividualWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_institution = sgqlc.types.Field(sgqlc.types.non_null('institution'), graphql_name='addInstitution', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('phone_number', sgqlc.types.Arg(Int, graphql_name='phone_number', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_institution = sgqlc.types.Field(sgqlc.types.non_null('institution'), graphql_name='updateInstitution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('phone_number', sgqlc.types.Arg(Int, graphql_name='phone_number', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('remove_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_institution = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteInstitution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_monitor = sgqlc.types.Field(sgqlc.types.non_null('monitor'), graphql_name='addMonitor', args=sgqlc.types.ArgDict((
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('second_last_name', sgqlc.types.Arg(String, graphql_name='second_last_name', default=None)),
        ('contact', sgqlc.types.Arg(String, graphql_name='contact', default=None)),
        ('add_cumulus_monitor', sgqlc.types.Arg(ID, graphql_name='addCumulus_monitor', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_monitor = sgqlc.types.Field(sgqlc.types.non_null('monitor'), graphql_name='updateMonitor', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('second_last_name', sgqlc.types.Arg(String, graphql_name='second_last_name', default=None)),
        ('contact', sgqlc.types.Arg(String, graphql_name='contact', default=None)),
        ('add_cumulus_monitor', sgqlc.types.Arg(ID, graphql_name='addCumulus_monitor', default=None)),
        ('remove_cumulus_monitor', sgqlc.types.Arg(ID, graphql_name='removeCumulus_monitor', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('remove_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeVisits', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_monitor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteMonitor', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_monitor_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateMonitorWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationMonitorWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_monitor_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateMonitorWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationMonitorWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_node = sgqlc.types.Field(sgqlc.types.non_null('node'), graphql_name='addNode', args=sgqlc.types.ArgDict((
        ('nomenclatura', sgqlc.types.Arg(String, graphql_name='nomenclatura', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('fid', sgqlc.types.Arg(Int, graphql_name='fid', default=None)),
        ('location', sgqlc.types.Arg(GeoJSONPointScalar, graphql_name='location', default=None)),
        ('cat_integr', sgqlc.types.Arg(String, graphql_name='cat_integr', default=None)),
        ('add_cumulus_node', sgqlc.types.Arg(ID, graphql_name='addCumulus_node', default=None)),
        ('add_unique_visit_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_pristine', default=None)),
        ('add_unique_visit_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_disturbed', default=None)),
        ('add_ecosystems', sgqlc.types.Arg(ID, graphql_name='addEcosystems', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('add_transects', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addTransects', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_node = sgqlc.types.Field(sgqlc.types.non_null('node'), graphql_name='updateNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('nomenclatura', sgqlc.types.Arg(String, graphql_name='nomenclatura', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('fid', sgqlc.types.Arg(Int, graphql_name='fid', default=None)),
        ('location', sgqlc.types.Arg(GeoJSONPointScalar, graphql_name='location', default=None)),
        ('cat_integr', sgqlc.types.Arg(String, graphql_name='cat_integr', default=None)),
        ('add_cumulus_node', sgqlc.types.Arg(ID, graphql_name='addCumulus_node', default=None)),
        ('remove_cumulus_node', sgqlc.types.Arg(ID, graphql_name='removeCumulus_node', default=None)),
        ('add_unique_visit_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_pristine', default=None)),
        ('remove_unique_visit_pristine', sgqlc.types.Arg(ID, graphql_name='removeUnique_visit_pristine', default=None)),
        ('add_unique_visit_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_disturbed', default=None)),
        ('remove_unique_visit_disturbed', sgqlc.types.Arg(ID, graphql_name='removeUnique_visit_disturbed', default=None)),
        ('add_ecosystems', sgqlc.types.Arg(ID, graphql_name='addEcosystems', default=None)),
        ('remove_ecosystems', sgqlc.types.Arg(ID, graphql_name='removeEcosystems', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('remove_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('remove_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeIndividuals', default=None)),
        ('add_transects', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addTransects', default=None)),
        ('remove_transects', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeTransects', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_node = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_node_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateNodeWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationNodeWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_node_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateNodeWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationNodeWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_node_with_ecosystem_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateNodeWithEcosystem_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationNodeWithEcosystem_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_node_with_ecosystem_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateNodeWithEcosystem_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationNodeWithEcosystem_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_physical_device = sgqlc.types.Field(sgqlc.types.non_null('physical_device'), graphql_name='addPhysical_device', args=sgqlc.types.ArgDict((
        ('serial_number', sgqlc.types.Arg(String, graphql_name='serial_number', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('previous_cumulus_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='previous_cumulus_ids', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('add_cumulus_device', sgqlc.types.Arg(ID, graphql_name='addCumulus_device', default=None)),
        ('add_device_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevice_deployments', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_physical_device = sgqlc.types.Field(sgqlc.types.non_null('physical_device'), graphql_name='updatePhysical_device', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('serial_number', sgqlc.types.Arg(String, graphql_name='serial_number', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('previous_cumulus_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='previous_cumulus_ids', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('remove_device', sgqlc.types.Arg(ID, graphql_name='removeDevice', default=None)),
        ('add_cumulus_device', sgqlc.types.Arg(ID, graphql_name='addCumulus_device', default=None)),
        ('remove_cumulus_device', sgqlc.types.Arg(ID, graphql_name='removeCumulus_device', default=None)),
        ('add_device_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevice_deployments', default=None)),
        ('remove_device_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDevice_deployments', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_physical_device = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deletePhysical_device', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_physical_device_with_device_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociatePhysical_deviceWithDevice_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationPhysical_deviceWithDevice_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_physical_device_with_device_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociatePhysical_deviceWithDevice_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationPhysical_deviceWithDevice_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_physical_device_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociatePhysical_deviceWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationPhysical_deviceWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_physical_device_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociatePhysical_deviceWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationPhysical_deviceWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_pipeline_info = sgqlc.types.Field(sgqlc.types.non_null('pipeline_info'), graphql_name='addPipeline_info', args=sgqlc.types.ArgDict((
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
        ('commit_dvc_of_data_ref', sgqlc.types.Arg(String, graphql_name='commit_dvc_of_data_ref', default=None)),
        ('url_repo_model', sgqlc.types.Arg(String, graphql_name='url_repo_model', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_pipeline_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPipeline_products', default=None)),
        ('add_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAnnotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_pipeline_info = sgqlc.types.Field(sgqlc.types.non_null('pipeline_info'), graphql_name='updatePipeline_info', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
        ('commit_dvc_of_data_ref', sgqlc.types.Arg(String, graphql_name='commit_dvc_of_data_ref', default=None)),
        ('url_repo_model', sgqlc.types.Arg(String, graphql_name='url_repo_model', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_pipeline_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPipeline_products', default=None)),
        ('remove_pipeline_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removePipeline_products', default=None)),
        ('add_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAnnotations', default=None)),
        ('remove_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeAnnotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_pipeline_info = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deletePipeline_info', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_product = sgqlc.types.Field(sgqlc.types.non_null('product'), graphql_name='addProduct', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('producer', sgqlc.types.Arg(String, graphql_name='producer', default=None)),
        ('project', sgqlc.types.Arg(String, graphql_name='project', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_file_assoc', sgqlc.types.Arg(ID, graphql_name='addFileAssoc', default=None)),
        ('add_pipeline', sgqlc.types.Arg(ID, graphql_name='addPipeline', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_product = sgqlc.types.Field(sgqlc.types.non_null('product'), graphql_name='updateProduct', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('producer', sgqlc.types.Arg(String, graphql_name='producer', default=None)),
        ('project', sgqlc.types.Arg(String, graphql_name='project', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_file_assoc', sgqlc.types.Arg(ID, graphql_name='addFileAssoc', default=None)),
        ('remove_file_assoc', sgqlc.types.Arg(ID, graphql_name='removeFileAssoc', default=None)),
        ('add_pipeline', sgqlc.types.Arg(ID, graphql_name='addPipeline', default=None)),
        ('remove_pipeline', sgqlc.types.Arg(ID, graphql_name='removePipeline', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_product = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteProduct', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_product_with_file_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateProductWithFile_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationProductWithFile_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_product_with_file_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateProductWithFile_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationProductWithFile_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_product_with_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateProductWithPipeline_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationProductWithPipeline_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_product_with_pipeline_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateProductWithPipeline_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationProductWithPipeline_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_role = sgqlc.types.Field(sgqlc.types.non_null('role'), graphql_name='addRole', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_role = sgqlc.types.Field(sgqlc.types.non_null('role'), graphql_name='updateRole', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('remove_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteRole', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_role_to_user = sgqlc.types.Field(sgqlc.types.non_null('role_to_user'), graphql_name='addRole_to_user', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(Int, graphql_name='user_id', default=None)),
        ('role_id', sgqlc.types.Arg(Int, graphql_name='role_id', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_role_to_user = sgqlc.types.Field(sgqlc.types.non_null('role_to_user'), graphql_name='updateRole_to_user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('user_id', sgqlc.types.Arg(Int, graphql_name='user_id', default=None)),
        ('role_id', sgqlc.types.Arg(Int, graphql_name='role_id', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_role_to_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteRole_to_user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_transect = sgqlc.types.Field(sgqlc.types.non_null('transect'), graphql_name='addTransect', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('sum_vegetation_structure', sgqlc.types.Arg(Float, graphql_name='sum_vegetation_structure', default=None)),
        ('sum_indicator_species', sgqlc.types.Arg(Float, graphql_name='sum_indicator_species', default=None)),
        ('sum_impact', sgqlc.types.Arg(Float, graphql_name='sum_impact', default=None)),
        ('date_transecto', sgqlc.types.Arg(DateTime, graphql_name='date_transecto', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('percentage', sgqlc.types.Arg(Float, graphql_name='percentage', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_transect = sgqlc.types.Field(sgqlc.types.non_null('transect'), graphql_name='updateTransect', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('sum_vegetation_structure', sgqlc.types.Arg(Float, graphql_name='sum_vegetation_structure', default=None)),
        ('sum_indicator_species', sgqlc.types.Arg(Float, graphql_name='sum_indicator_species', default=None)),
        ('sum_impact', sgqlc.types.Arg(Float, graphql_name='sum_impact', default=None)),
        ('date_transecto', sgqlc.types.Arg(DateTime, graphql_name='date_transecto', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('percentage', sgqlc.types.Arg(Float, graphql_name='percentage', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('remove_associated_node', sgqlc.types.Arg(ID, graphql_name='removeAssociated_node', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_transect = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteTransect', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_transect_with_node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateTransectWithNode_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationTransectWithNode_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_transect_with_node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateTransectWithNode_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationTransectWithNode_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_user = sgqlc.types.Field(sgqlc.types.non_null('user'), graphql_name='addUser', args=sgqlc.types.ArgDict((
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='is_active', default=None)),
        ('last_login', sgqlc.types.Arg(DateTime, graphql_name='last_login', default=None)),
        ('add_institutions', sgqlc.types.Arg(ID, graphql_name='addInstitutions', default=None)),
        ('add_roles', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addRoles', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_cumulus', default=None)),
        ('add_user_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUser_annotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_user = sgqlc.types.Field(sgqlc.types.non_null('user'), graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='is_active', default=None)),
        ('last_login', sgqlc.types.Arg(DateTime, graphql_name='last_login', default=None)),
        ('add_institutions', sgqlc.types.Arg(ID, graphql_name='addInstitutions', default=None)),
        ('remove_institutions', sgqlc.types.Arg(ID, graphql_name='removeInstitutions', default=None)),
        ('add_roles', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addRoles', default=None)),
        ('remove_roles', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeRoles', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_cumulus', default=None)),
        ('remove_associated_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeAssociated_cumulus', default=None)),
        ('add_user_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUser_annotations', default=None)),
        ('remove_user_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUser_annotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_user_with_institution_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateUserWithInstitution_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationUserWithInstitution_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_user_with_institution_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateUserWithInstitution_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationUserWithInstitution_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    add_visit = sgqlc.types.Field(sgqlc.types.non_null('visit'), graphql_name='addVisit', args=sgqlc.types.ArgDict((
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('date_sipecam_first_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_first_season', default=None)),
        ('date_sipecam_second_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_second_season', default=None)),
        ('date_first_season', sgqlc.types.Arg(Date, graphql_name='date_first_season', default=None)),
        ('date_second_season', sgqlc.types.Arg(Date, graphql_name='date_second_season', default=None)),
        ('report_first_season', sgqlc.types.Arg(String, graphql_name='report_first_season', default=None)),
        ('report_second_season', sgqlc.types.Arg(String, graphql_name='report_second_season', default=None)),
        ('add_cumulus_visit', sgqlc.types.Arg(ID, graphql_name='addCumulus_visit', default=None)),
        ('add_unique_node_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_node_pristine', default=None)),
        ('add_unique_node_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_node_disturbed', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    update_visit = sgqlc.types.Field(sgqlc.types.non_null('visit'), graphql_name='updateVisit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('date_sipecam_first_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_first_season', default=None)),
        ('date_sipecam_second_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_second_season', default=None)),
        ('date_first_season', sgqlc.types.Arg(Date, graphql_name='date_first_season', default=None)),
        ('date_second_season', sgqlc.types.Arg(Date, graphql_name='date_second_season', default=None)),
        ('report_first_season', sgqlc.types.Arg(String, graphql_name='report_first_season', default=None)),
        ('report_second_season', sgqlc.types.Arg(String, graphql_name='report_second_season', default=None)),
        ('add_cumulus_visit', sgqlc.types.Arg(ID, graphql_name='addCumulus_visit', default=None)),
        ('remove_cumulus_visit', sgqlc.types.Arg(ID, graphql_name='removeCumulus_visit', default=None)),
        ('add_unique_node_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_node_pristine', default=None)),
        ('remove_unique_node_pristine', sgqlc.types.Arg(ID, graphql_name='removeUnique_node_pristine', default=None)),
        ('add_unique_node_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_node_disturbed', default=None)),
        ('remove_unique_node_disturbed', sgqlc.types.Arg(ID, graphql_name='removeUnique_node_disturbed', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('remove_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeMonitors', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    delete_visit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteVisit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_associate_visit_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateVisitWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationVisitWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_visit_with_cumulus_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateVisitWithCumulus_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationVisitWithCumulus_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_visit_with_pristine_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateVisitWithPristine_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationVisitWithPristine_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_visit_with_pristine_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateVisitWithPristine_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationVisitWithPristine_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_associate_visit_with_disturbed_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkAssociateVisitWithDisturbed_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationVisitWithDisturbed_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    bulk_dis_associate_visit_with_disturbed_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bulkDisAssociateVisitWithDisturbed_id', args=sgqlc.types.ArgDict((
        ('bulk_association_input', sgqlc.types.Arg(sgqlc.types.list_of(bulkAssociationVisitWithDisturbed_idInput), graphql_name='bulkAssociationInput', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )


class NodeConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('NodeEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('node'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class NodeEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('node'), graphql_name='node')


class Physical_deviceConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'physical_devices', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('Physical_deviceEdge'), graphql_name='edges')
    physical_devices = sgqlc.types.Field(sgqlc.types.list_of('physical_device'), graphql_name='physical_devices')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class Physical_deviceEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('physical_device'), graphql_name='node')


class Pipeline_infoConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'pipeline_infos', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('Pipeline_infoEdge'), graphql_name='edges')
    pipeline_infos = sgqlc.types.Field(sgqlc.types.list_of('pipeline_info'), graphql_name='pipeline_infos')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class Pipeline_infoEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('pipeline_info'), graphql_name='node')


class ProductConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'products', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProductEdge'), graphql_name='edges')
    products = sgqlc.types.Field(sgqlc.types.list_of('product'), graphql_name='products')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class ProductEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('product'), graphql_name='node')


class Query(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('annotations_geom_obs_types', 'read_one_annotations_geom_obs_type', 'count_annotations_geom_obs_types', 'csv_table_template_annotations_geom_obs_type', 'annotations_geom_obs_types_connection', 'validate_annotations_geom_obs_type_for_creation', 'validate_annotations_geom_obs_type_for_updating', 'validate_annotations_geom_obs_type_for_deletion', 'validate_annotations_geom_obs_type_after_reading', 'annotations_geom_obs_types_zendro_definition', 'calendars', 'read_one_calendar', 'count_calendars', 'csv_table_template_calendar', 'calendars_connection', 'validate_calendar_for_creation', 'validate_calendar_for_updating', 'validate_calendar_for_deletion', 'validate_calendar_after_reading', 'calendars_zendro_definition', 'cumulus', 'read_one_cumulus', 'count_cumulus', 'csv_table_template_cumulus', 'cumulus_connection', 'validate_cumulus_for_creation', 'validate_cumulus_for_updating', 'validate_cumulus_for_deletion', 'validate_cumulus_after_reading', 'cumulus_zendro_definition', 'cumulus_criteria', 'read_one_cumulus_criteria', 'count_cumulus_criteria', 'csv_table_template_cumulus_criteria', 'cumulus_criteria_connection', 'validate_cumulus_criteria_for_creation', 'validate_cumulus_criteria_for_updating', 'validate_cumulus_criteria_for_deletion', 'validate_cumulus_criteria_after_reading', 'cumulus_criteria_zendro_definition', 'ecosystem_file_counts', 'deployments', 'read_one_deployment', 'count_deployments', 'csv_table_template_deployment', 'deployments_connection', 'validate_deployment_for_creation', 'validate_deployment_for_updating', 'validate_deployment_for_deletion', 'validate_deployment_after_reading', 'deployments_zendro_definition', 'device_catalogs', 'read_one_device_catalog', 'count_device_catalogs', 'csv_table_template_device_catalog', 'device_catalogs_connection', 'validate_device_catalog_for_creation', 'validate_device_catalog_for_updating', 'validate_device_catalog_for_deletion', 'validate_device_catalog_after_reading', 'device_catalogs_zendro_definition', 'ecosystems', 'read_one_ecosystem', 'count_ecosystems', 'csv_table_template_ecosystem', 'ecosystems_connection', 'validate_ecosystem_for_creation', 'validate_ecosystem_for_updating', 'validate_ecosystem_for_deletion', 'validate_ecosystem_after_reading', 'ecosystems_zendro_definition', 'files', 'read_one_file', 'count_files', 'csv_table_template_file', 'files_connection', 'validate_file_for_creation', 'validate_file_for_updating', 'validate_file_for_deletion', 'validate_file_after_reading', 'files_zendro_definition', 'file_counts', 'read_one_file_count', 'count_file_counts', 'csv_table_template_file_count', 'file_counts_connection', 'validate_file_count_for_creation', 'validate_file_count_for_updating', 'validate_file_count_for_deletion', 'validate_file_count_after_reading', 'file_counts_zendro_definition', 'individuals', 'read_one_individual', 'count_individuals', 'csv_table_template_individual', 'individuals_connection', 'validate_individual_for_creation', 'validate_individual_for_updating', 'validate_individual_for_deletion', 'validate_individual_after_reading', 'individuals_zendro_definition', 'institutions', 'read_one_institution', 'count_institutions', 'csv_table_template_institution', 'institutions_connection', 'validate_institution_for_creation', 'validate_institution_for_updating', 'validate_institution_for_deletion', 'validate_institution_after_reading', 'institutions_zendro_definition', 'monitors', 'read_one_monitor', 'count_monitors', 'csv_table_template_monitor', 'monitors_connection', 'validate_monitor_for_creation', 'validate_monitor_for_updating', 'validate_monitor_for_deletion', 'validate_monitor_after_reading', 'monitors_zendro_definition', 'nodes', 'read_one_node', 'count_nodes', 'csv_table_template_node', 'nodes_connection', 'validate_node_for_creation', 'validate_node_for_updating', 'validate_node_for_deletion', 'validate_node_after_reading', 'nodes_zendro_definition', 'physical_devices', 'read_one_physical_device', 'count_physical_devices', 'csv_table_template_physical_device', 'physical_devices_connection', 'validate_physical_device_for_creation', 'validate_physical_device_for_updating', 'validate_physical_device_for_deletion', 'validate_physical_device_after_reading', 'physical_devices_zendro_definition', 'pipeline_infos', 'read_one_pipeline_info', 'count_pipeline_infos', 'csv_table_template_pipeline_info', 'pipeline_infos_connection', 'validate_pipeline_info_for_creation', 'validate_pipeline_info_for_updating', 'validate_pipeline_info_for_deletion', 'validate_pipeline_info_after_reading', 'pipeline_infos_zendro_definition', 'products', 'read_one_product', 'count_products', 'csv_table_template_product', 'products_connection', 'validate_product_for_creation', 'validate_product_for_updating', 'validate_product_for_deletion', 'validate_product_after_reading', 'products_zendro_definition', 'roles', 'read_one_role', 'count_roles', 'csv_table_template_role', 'roles_connection', 'validate_role_for_creation', 'validate_role_for_updating', 'validate_role_for_deletion', 'validate_role_after_reading', 'roles_zendro_definition', 'role_to_users', 'read_one_role_to_user', 'count_role_to_users', 'csv_table_template_role_to_user', 'role_to_users_connection', 'validate_role_to_user_for_creation', 'validate_role_to_user_for_updating', 'validate_role_to_user_for_deletion', 'validate_role_to_user_after_reading', 'role_to_users_zendro_definition', 'transects', 'read_one_transect', 'count_transects', 'csv_table_template_transect', 'transects_connection', 'validate_transect_for_creation', 'validate_transect_for_updating', 'validate_transect_for_deletion', 'validate_transect_after_reading', 'transects_zendro_definition', 'users', 'read_one_user', 'count_users', 'csv_table_template_user', 'users_connection', 'validate_user_for_creation', 'validate_user_for_updating', 'validate_user_for_deletion', 'validate_user_after_reading', 'users_zendro_definition', 'visits', 'read_one_visit', 'count_visits', 'csv_table_template_visit', 'visits_connection', 'validate_visit_for_creation', 'validate_visit_for_updating', 'validate_visit_for_deletion', 'validate_visit_after_reading', 'visits_zendro_definition')
    annotations_geom_obs_types = sgqlc.types.Field(sgqlc.types.list_of('annotations_geom_obs_type'), graphql_name='annotations_geom_obs_types', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_annotations_geom_obs_type = sgqlc.types.Field('annotations_geom_obs_type', graphql_name='readOneAnnotations_geom_obs_type', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_annotations_geom_obs_types = sgqlc.types.Field(Int, graphql_name='countAnnotations_geom_obs_types', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_annotations_geom_obs_type = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateAnnotations_geom_obs_type')
    annotations_geom_obs_types_connection = sgqlc.types.Field(Annotations_geom_obs_typeConnection, graphql_name='annotations_geom_obs_typesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_annotations_geom_obs_type_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateAnnotations_geom_obs_typeForCreation', args=sgqlc.types.ArgDict((
        ('classified_by', sgqlc.types.Arg(String, graphql_name='classified_by', default=None)),
        ('classification_method', sgqlc.types.Arg(String, graphql_name='classification_method', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('confidence', sgqlc.types.Arg(Float, graphql_name='confidence', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONGeometryCollectionScalar, graphql_name='geometry', default=None)),
        ('video_frame_num', sgqlc.types.Arg(Int, graphql_name='video_frame_num', default=None)),
        ('frequency_min', sgqlc.types.Arg(Float, graphql_name='frequency_min', default=None)),
        ('frequency_max', sgqlc.types.Arg(Float, graphql_name='frequency_max', default=None)),
        ('time_min', sgqlc.types.Arg(Float, graphql_name='time_min', default=None)),
        ('time_max', sgqlc.types.Arg(Float, graphql_name='time_max', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_file_to', sgqlc.types.Arg(ID, graphql_name='addFileTo', default=None)),
        ('add_user_to', sgqlc.types.Arg(ID, graphql_name='addUserTo', default=None)),
        ('add_pipeline_annotation', sgqlc.types.Arg(ID, graphql_name='addPipeline_annotation', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_annotations_geom_obs_type_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateAnnotations_geom_obs_typeForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('classified_by', sgqlc.types.Arg(String, graphql_name='classified_by', default=None)),
        ('classification_method', sgqlc.types.Arg(String, graphql_name='classification_method', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('confidence', sgqlc.types.Arg(Float, graphql_name='confidence', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONGeometryCollectionScalar, graphql_name='geometry', default=None)),
        ('video_frame_num', sgqlc.types.Arg(Int, graphql_name='video_frame_num', default=None)),
        ('frequency_min', sgqlc.types.Arg(Float, graphql_name='frequency_min', default=None)),
        ('frequency_max', sgqlc.types.Arg(Float, graphql_name='frequency_max', default=None)),
        ('time_min', sgqlc.types.Arg(Float, graphql_name='time_min', default=None)),
        ('time_max', sgqlc.types.Arg(Float, graphql_name='time_max', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_file_to', sgqlc.types.Arg(ID, graphql_name='addFileTo', default=None)),
        ('remove_file_to', sgqlc.types.Arg(ID, graphql_name='removeFileTo', default=None)),
        ('add_user_to', sgqlc.types.Arg(ID, graphql_name='addUserTo', default=None)),
        ('remove_user_to', sgqlc.types.Arg(ID, graphql_name='removeUserTo', default=None)),
        ('add_pipeline_annotation', sgqlc.types.Arg(ID, graphql_name='addPipeline_annotation', default=None)),
        ('remove_pipeline_annotation', sgqlc.types.Arg(ID, graphql_name='removePipeline_annotation', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_annotations_geom_obs_type_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateAnnotations_geom_obs_typeForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_annotations_geom_obs_type_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateAnnotations_geom_obs_typeAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    annotations_geom_obs_types_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='annotations_geom_obs_typesZendroDefinition')
    calendars = sgqlc.types.Field(sgqlc.types.list_of('calendar'), graphql_name='calendars', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCalendarInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCalendarInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_calendar = sgqlc.types.Field('calendar', graphql_name='readOneCalendar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_calendars = sgqlc.types.Field(Int, graphql_name='countCalendars', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCalendarInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_calendar = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateCalendar')
    calendars_connection = sgqlc.types.Field(CalendarConnection, graphql_name='calendarsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCalendarInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCalendarInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_calendar_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCalendarForCreation', args=sgqlc.types.ArgDict((
        ('date_started', sgqlc.types.Arg(Date, graphql_name='date_started', default=None)),
        ('date_finished', sgqlc.types.Arg(Date, graphql_name='date_finished', default=None)),
        ('sipecam_year', sgqlc.types.Arg(String, graphql_name='sipecam_year', default=None)),
        ('order', sgqlc.types.Arg(Int, graphql_name='order', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_calendar_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCalendarForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date_started', sgqlc.types.Arg(Date, graphql_name='date_started', default=None)),
        ('date_finished', sgqlc.types.Arg(Date, graphql_name='date_finished', default=None)),
        ('sipecam_year', sgqlc.types.Arg(String, graphql_name='sipecam_year', default=None)),
        ('order', sgqlc.types.Arg(Int, graphql_name='order', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_calendar_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCalendarForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_calendar_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCalendarAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    calendars_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='calendarsZendroDefinition')
    cumulus = sgqlc.types.Field(sgqlc.types.list_of('cumulus'), graphql_name='cumulus', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_cumulus = sgqlc.types.Field('cumulus', graphql_name='readOneCumulus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_cumulus = sgqlc.types.Field(Int, graphql_name='countCumulus', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_cumulus = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateCumulus')
    cumulus_connection = sgqlc.types.Field(CumulusConnection, graphql_name='cumulusConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_cumulus_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulusForCreation', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONPolygonScalar, graphql_name='geometry', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('add_cumulus_criteria', sgqlc.types.Arg(ID, graphql_name='addCumulus_criteria', default=None)),
        ('add_unique_ecosystem', sgqlc.types.Arg(ID, graphql_name='addUnique_ecosystem', default=None)),
        ('add_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevices', default=None)),
        ('add_associated_partners', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_partners', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('add_nodes', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addNodes', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('add_file_counts', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_counts', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_cumulus_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulusForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('geometry', sgqlc.types.Arg(GeoJSONPolygonScalar, graphql_name='geometry', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('add_cumulus_criteria', sgqlc.types.Arg(ID, graphql_name='addCumulus_criteria', default=None)),
        ('remove_cumulus_criteria', sgqlc.types.Arg(ID, graphql_name='removeCumulus_criteria', default=None)),
        ('add_unique_ecosystem', sgqlc.types.Arg(ID, graphql_name='addUnique_ecosystem', default=None)),
        ('remove_unique_ecosystem', sgqlc.types.Arg(ID, graphql_name='removeUnique_ecosystem', default=None)),
        ('add_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevices', default=None)),
        ('remove_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDevices', default=None)),
        ('add_associated_partners', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_partners', default=None)),
        ('remove_associated_partners', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeAssociated_partners', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('remove_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeVisits', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('remove_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeMonitors', default=None)),
        ('add_nodes', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addNodes', default=None)),
        ('remove_nodes', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeNodes', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('remove_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('remove_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeIndividuals', default=None)),
        ('add_file_counts', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_counts', default=None)),
        ('remove_file_counts', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFile_counts', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_cumulus_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulusForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_cumulus_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulusAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    cumulus_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='cumulusZendroDefinition')
    cumulus_criteria = sgqlc.types.Field(sgqlc.types.list_of('cumulus_criteria'), graphql_name='cumulus_criteria', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulus_criteriaInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulus_criteriaInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_cumulus_criteria = sgqlc.types.Field('cumulus_criteria', graphql_name='readOneCumulus_criteria', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_cumulus_criteria = sgqlc.types.Field(Int, graphql_name='countCumulus_criteria', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulus_criteriaInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_cumulus_criteria = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateCumulus_criteria')
    cumulus_criteria_connection = sgqlc.types.Field(Cumulus_criteriaConnection, graphql_name='cumulus_criteriaConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulus_criteriaInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulus_criteriaInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_cumulus_criteria_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulus_criteriaForCreation', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_cumulus_criteria_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulus_criteriaForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus', default=None)),
        ('remove_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeCumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_cumulus_criteria_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulus_criteriaForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_cumulus_criteria_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateCumulus_criteriaAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    cumulus_criteria_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='cumulus_criteriaZendroDefinition')
    ecosystem_file_counts = sgqlc.types.Field('ecosystem_files', graphql_name='ecosystemFileCounts', args=sgqlc.types.ArgDict((
        ('ecosystem_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='ecosystem_id', default=None)),
))
    )
    deployments = sgqlc.types.Field(sgqlc.types.list_of('deployment'), graphql_name='deployments', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_deployment = sgqlc.types.Field('deployment', graphql_name='readOneDeployment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_deployments = sgqlc.types.Field(Int, graphql_name='countDeployments', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_deployment = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateDeployment')
    deployments_connection = sgqlc.types.Field(DeploymentConnection, graphql_name='deploymentsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_deployment_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDeploymentForCreation', args=sgqlc.types.ArgDict((
        ('date_deployment', sgqlc.types.Arg(DateTime, graphql_name='date_deployment', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('add_node', sgqlc.types.Arg(ID, graphql_name='addNode', default=None)),
        ('add_cumulus', sgqlc.types.Arg(ID, graphql_name='addCumulus', default=None)),
        ('add_files', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFiles', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_deployment_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDeploymentForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date_deployment', sgqlc.types.Arg(DateTime, graphql_name='date_deployment', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('remove_device', sgqlc.types.Arg(ID, graphql_name='removeDevice', default=None)),
        ('add_node', sgqlc.types.Arg(ID, graphql_name='addNode', default=None)),
        ('remove_node', sgqlc.types.Arg(ID, graphql_name='removeNode', default=None)),
        ('add_cumulus', sgqlc.types.Arg(ID, graphql_name='addCumulus', default=None)),
        ('remove_cumulus', sgqlc.types.Arg(ID, graphql_name='removeCumulus', default=None)),
        ('add_files', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFiles', default=None)),
        ('remove_files', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFiles', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_deployment_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDeploymentForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_deployment_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDeploymentAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    deployments_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='deploymentsZendroDefinition')
    device_catalogs = sgqlc.types.Field(sgqlc.types.list_of('device_catalog'), graphql_name='device_catalogs', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDevice_catalogInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDevice_catalogInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_device_catalog = sgqlc.types.Field('device_catalog', graphql_name='readOneDevice_catalog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_device_catalogs = sgqlc.types.Field(Int, graphql_name='countDevice_catalogs', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDevice_catalogInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_device_catalog = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateDevice_catalog')
    device_catalogs_connection = sgqlc.types.Field(Device_catalogConnection, graphql_name='device_catalogsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDevice_catalogInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDevice_catalogInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_device_catalog_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDevice_catalogForCreation', args=sgqlc.types.ArgDict((
        ('brand', sgqlc.types.Arg(String, graphql_name='brand', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('add_physical_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPhysical_devices', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_device_catalog_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDevice_catalogForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('brand', sgqlc.types.Arg(String, graphql_name='brand', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('add_physical_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPhysical_devices', default=None)),
        ('remove_physical_devices', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removePhysical_devices', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_device_catalog_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDevice_catalogForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_device_catalog_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateDevice_catalogAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    device_catalogs_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='device_catalogsZendroDefinition')
    ecosystems = sgqlc.types.Field(sgqlc.types.list_of('ecosystem'), graphql_name='ecosystems', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchEcosystemInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderEcosystemInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_ecosystem = sgqlc.types.Field('ecosystem', graphql_name='readOneEcosystem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_ecosystems = sgqlc.types.Field(Int, graphql_name='countEcosystems', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchEcosystemInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_ecosystem = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateEcosystem')
    ecosystems_connection = sgqlc.types.Field(EcosystemConnection, graphql_name='ecosystemsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchEcosystemInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderEcosystemInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_ecosystem_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateEcosystemForCreation', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_unique_node', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUnique_node', default=None)),
        ('add_cumulus_ecosystem', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus_ecosystem', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_ecosystem_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateEcosystemForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('add_unique_node', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUnique_node', default=None)),
        ('remove_unique_node', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUnique_node', default=None)),
        ('add_cumulus_ecosystem', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addCumulus_ecosystem', default=None)),
        ('remove_cumulus_ecosystem', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeCumulus_ecosystem', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_ecosystem_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateEcosystemForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_ecosystem_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateEcosystemAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    ecosystems_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='ecosystemsZendroDefinition')
    files = sgqlc.types.Field(sgqlc.types.list_of('file'), graphql_name='files', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFileInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_file = sgqlc.types.Field('file', graphql_name='readOneFile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_files = sgqlc.types.Field(Int, graphql_name='countFiles', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_file = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateFile')
    files_connection = sgqlc.types.Field(FileConnection, graphql_name='filesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFileInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_file_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFileForCreation', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('date_deployment_device', sgqlc.types.Arg(Date, graphql_name='date_deployment_device', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('id_alfresco', sgqlc.types.Arg(String, graphql_name='id_alfresco', default=None)),
        ('storage', sgqlc.types.Arg(String, graphql_name='storage', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_associated_deployment', sgqlc.types.Arg(ID, graphql_name='addAssociated_deployment', default=None)),
        ('add_file_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_annotations', default=None)),
        ('add_file_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_products', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_file_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFileForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('date_deployment_device', sgqlc.types.Arg(Date, graphql_name='date_deployment_device', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('id_alfresco', sgqlc.types.Arg(String, graphql_name='id_alfresco', default=None)),
        ('storage', sgqlc.types.Arg(String, graphql_name='storage', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('add_associated_deployment', sgqlc.types.Arg(ID, graphql_name='addAssociated_deployment', default=None)),
        ('remove_associated_deployment', sgqlc.types.Arg(ID, graphql_name='removeAssociated_deployment', default=None)),
        ('add_file_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_annotations', default=None)),
        ('remove_file_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFile_annotations', default=None)),
        ('add_file_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addFile_products', default=None)),
        ('remove_file_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeFile_products', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_file_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFileForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_file_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFileAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    files_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='filesZendroDefinition')
    file_counts = sgqlc.types.Field(sgqlc.types.list_of('file_count'), graphql_name='file_counts', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFile_countInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFile_countInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_file_count = sgqlc.types.Field('file_count', graphql_name='readOneFile_count', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_file_counts = sgqlc.types.Field(Int, graphql_name='countFile_counts', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFile_countInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_file_count = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateFile_count')
    file_counts_connection = sgqlc.types.Field(File_countConnection, graphql_name='file_countsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFile_countInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFile_countInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_file_count_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFile_countForCreation', args=sgqlc.types.ArgDict((
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='delivery_date', default=None)),
        ('audio_files', sgqlc.types.Arg(Int, graphql_name='audio_files', default=None)),
        ('image_files', sgqlc.types.Arg(Int, graphql_name='image_files', default=None)),
        ('video_files', sgqlc.types.Arg(Int, graphql_name='video_files', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
        ('add_cumulus_files', sgqlc.types.Arg(ID, graphql_name='addCumulus_files', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_file_count_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFile_countForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('delivery_date', sgqlc.types.Arg(Date, graphql_name='delivery_date', default=None)),
        ('audio_files', sgqlc.types.Arg(Int, graphql_name='audio_files', default=None)),
        ('image_files', sgqlc.types.Arg(Int, graphql_name='image_files', default=None)),
        ('video_files', sgqlc.types.Arg(Int, graphql_name='video_files', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
        ('add_cumulus_files', sgqlc.types.Arg(ID, graphql_name='addCumulus_files', default=None)),
        ('remove_cumulus_files', sgqlc.types.Arg(ID, graphql_name='removeCumulus_files', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_file_count_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFile_countForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_file_count_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateFile_countAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    file_counts_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='file_countsZendroDefinition')
    individuals = sgqlc.types.Field(sgqlc.types.list_of('individual'), graphql_name='individuals', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderIndividualInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_individual = sgqlc.types.Field('individual', graphql_name='readOneIndividual', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_individuals = sgqlc.types.Field(Int, graphql_name='countIndividuals', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_individual = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateIndividual')
    individuals_connection = sgqlc.types.Field(IndividualConnection, graphql_name='individualsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderIndividualInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_individual_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateIndividualForCreation', args=sgqlc.types.ArgDict((
        ('date_trap', sgqlc.types.Arg(DateTime, graphql_name='date_trap', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('clave_posicion_malla', sgqlc.types.Arg(String, graphql_name='clave_posicion_malla', default=None)),
        ('arete', sgqlc.types.Arg(Int, graphql_name='arete', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(ID, graphql_name='addAssociated_cumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_individual_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateIndividualForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date_trap', sgqlc.types.Arg(DateTime, graphql_name='date_trap', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('altitude', sgqlc.types.Arg(Float, graphql_name='altitude', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('kobo_url', sgqlc.types.Arg(String, graphql_name='kobo_url', default=None)),
        ('clave_posicion_malla', sgqlc.types.Arg(String, graphql_name='clave_posicion_malla', default=None)),
        ('arete', sgqlc.types.Arg(Int, graphql_name='arete', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('remove_associated_node', sgqlc.types.Arg(ID, graphql_name='removeAssociated_node', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(ID, graphql_name='addAssociated_cumulus', default=None)),
        ('remove_associated_cumulus', sgqlc.types.Arg(ID, graphql_name='removeAssociated_cumulus', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_individual_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateIndividualForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_individual_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateIndividualAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    individuals_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='individualsZendroDefinition')
    institutions = sgqlc.types.Field(sgqlc.types.list_of('institution'), graphql_name='institutions', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchInstitutionInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderInstitutionInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_institution = sgqlc.types.Field('institution', graphql_name='readOneInstitution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_institutions = sgqlc.types.Field(Int, graphql_name='countInstitutions', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchInstitutionInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_institution = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateInstitution')
    institutions_connection = sgqlc.types.Field(InstitutionConnection, graphql_name='institutionsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchInstitutionInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderInstitutionInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_institution_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateInstitutionForCreation', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('phone_number', sgqlc.types.Arg(Int, graphql_name='phone_number', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_institution_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateInstitutionForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('phone_number', sgqlc.types.Arg(Int, graphql_name='phone_number', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('remove_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_institution_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateInstitutionForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_institution_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateInstitutionAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    institutions_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='institutionsZendroDefinition')
    monitors = sgqlc.types.Field(sgqlc.types.list_of('monitor'), graphql_name='monitors', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderMonitorInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_monitor = sgqlc.types.Field('monitor', graphql_name='readOneMonitor', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_monitors = sgqlc.types.Field(Int, graphql_name='countMonitors', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_monitor = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateMonitor')
    monitors_connection = sgqlc.types.Field(MonitorConnection, graphql_name='monitorsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderMonitorInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_monitor_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateMonitorForCreation', args=sgqlc.types.ArgDict((
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('second_last_name', sgqlc.types.Arg(String, graphql_name='second_last_name', default=None)),
        ('contact', sgqlc.types.Arg(String, graphql_name='contact', default=None)),
        ('add_cumulus_monitor', sgqlc.types.Arg(ID, graphql_name='addCumulus_monitor', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_monitor_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateMonitorForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('second_last_name', sgqlc.types.Arg(String, graphql_name='second_last_name', default=None)),
        ('contact', sgqlc.types.Arg(String, graphql_name='contact', default=None)),
        ('add_cumulus_monitor', sgqlc.types.Arg(ID, graphql_name='addCumulus_monitor', default=None)),
        ('remove_cumulus_monitor', sgqlc.types.Arg(ID, graphql_name='removeCumulus_monitor', default=None)),
        ('add_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addVisits', default=None)),
        ('remove_visits', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeVisits', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_monitor_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateMonitorForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_monitor_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateMonitorAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    monitors_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='monitorsZendroDefinition')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('node'), graphql_name='nodes', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderNodeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_node = sgqlc.types.Field('node', graphql_name='readOneNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_nodes = sgqlc.types.Field(Int, graphql_name='countNodes', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_node = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateNode')
    nodes_connection = sgqlc.types.Field(NodeConnection, graphql_name='nodesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderNodeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_node_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateNodeForCreation', args=sgqlc.types.ArgDict((
        ('nomenclatura', sgqlc.types.Arg(String, graphql_name='nomenclatura', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('fid', sgqlc.types.Arg(Int, graphql_name='fid', default=None)),
        ('location', sgqlc.types.Arg(GeoJSONPointScalar, graphql_name='location', default=None)),
        ('cat_integr', sgqlc.types.Arg(String, graphql_name='cat_integr', default=None)),
        ('add_cumulus_node', sgqlc.types.Arg(ID, graphql_name='addCumulus_node', default=None)),
        ('add_unique_visit_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_pristine', default=None)),
        ('add_unique_visit_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_disturbed', default=None)),
        ('add_ecosystems', sgqlc.types.Arg(ID, graphql_name='addEcosystems', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('add_transects', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addTransects', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_node_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateNodeForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('nomenclatura', sgqlc.types.Arg(String, graphql_name='nomenclatura', default=None)),
        ('con_socio', sgqlc.types.Arg(Int, graphql_name='con_socio', default=None)),
        ('fid', sgqlc.types.Arg(Int, graphql_name='fid', default=None)),
        ('location', sgqlc.types.Arg(GeoJSONPointScalar, graphql_name='location', default=None)),
        ('cat_integr', sgqlc.types.Arg(String, graphql_name='cat_integr', default=None)),
        ('add_cumulus_node', sgqlc.types.Arg(ID, graphql_name='addCumulus_node', default=None)),
        ('remove_cumulus_node', sgqlc.types.Arg(ID, graphql_name='removeCumulus_node', default=None)),
        ('add_unique_visit_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_pristine', default=None)),
        ('remove_unique_visit_pristine', sgqlc.types.Arg(ID, graphql_name='removeUnique_visit_pristine', default=None)),
        ('add_unique_visit_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_visit_disturbed', default=None)),
        ('remove_unique_visit_disturbed', sgqlc.types.Arg(ID, graphql_name='removeUnique_visit_disturbed', default=None)),
        ('add_ecosystems', sgqlc.types.Arg(ID, graphql_name='addEcosystems', default=None)),
        ('remove_ecosystems', sgqlc.types.Arg(ID, graphql_name='removeEcosystems', default=None)),
        ('add_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDeployments', default=None)),
        ('remove_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDeployments', default=None)),
        ('add_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addIndividuals', default=None)),
        ('remove_individuals', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeIndividuals', default=None)),
        ('add_transects', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addTransects', default=None)),
        ('remove_transects', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeTransects', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_node_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateNodeForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_node_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateNodeAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    nodes_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='nodesZendroDefinition')
    physical_devices = sgqlc.types.Field(sgqlc.types.list_of('physical_device'), graphql_name='physical_devices', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPhysical_deviceInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_physical_device = sgqlc.types.Field('physical_device', graphql_name='readOnePhysical_device', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_physical_devices = sgqlc.types.Field(Int, graphql_name='countPhysical_devices', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_physical_device = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplatePhysical_device')
    physical_devices_connection = sgqlc.types.Field(Physical_deviceConnection, graphql_name='physical_devicesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPhysical_deviceInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_physical_device_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePhysical_deviceForCreation', args=sgqlc.types.ArgDict((
        ('serial_number', sgqlc.types.Arg(String, graphql_name='serial_number', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('previous_cumulus_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='previous_cumulus_ids', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('add_cumulus_device', sgqlc.types.Arg(ID, graphql_name='addCumulus_device', default=None)),
        ('add_device_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevice_deployments', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_physical_device_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePhysical_deviceForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('serial_number', sgqlc.types.Arg(String, graphql_name='serial_number', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('previous_cumulus_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='previous_cumulus_ids', default=None)),
        ('add_device', sgqlc.types.Arg(ID, graphql_name='addDevice', default=None)),
        ('remove_device', sgqlc.types.Arg(ID, graphql_name='removeDevice', default=None)),
        ('add_cumulus_device', sgqlc.types.Arg(ID, graphql_name='addCumulus_device', default=None)),
        ('remove_cumulus_device', sgqlc.types.Arg(ID, graphql_name='removeCumulus_device', default=None)),
        ('add_device_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addDevice_deployments', default=None)),
        ('remove_device_deployments', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeDevice_deployments', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_physical_device_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePhysical_deviceForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_physical_device_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePhysical_deviceAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    physical_devices_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='physical_devicesZendroDefinition')
    pipeline_infos = sgqlc.types.Field(sgqlc.types.list_of('pipeline_info'), graphql_name='pipeline_infos', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPipeline_infoInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPipeline_infoInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_pipeline_info = sgqlc.types.Field('pipeline_info', graphql_name='readOnePipeline_info', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_pipeline_infos = sgqlc.types.Field(Int, graphql_name='countPipeline_infos', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPipeline_infoInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_pipeline_info = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplatePipeline_info')
    pipeline_infos_connection = sgqlc.types.Field(Pipeline_infoConnection, graphql_name='pipeline_infosConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPipeline_infoInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPipeline_infoInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_pipeline_info_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePipeline_infoForCreation', args=sgqlc.types.ArgDict((
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
        ('commit_dvc_of_data_ref', sgqlc.types.Arg(String, graphql_name='commit_dvc_of_data_ref', default=None)),
        ('url_repo_model', sgqlc.types.Arg(String, graphql_name='url_repo_model', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_pipeline_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPipeline_products', default=None)),
        ('add_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAnnotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_pipeline_info_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePipeline_infoForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
        ('commit_dvc_of_data_ref', sgqlc.types.Arg(String, graphql_name='commit_dvc_of_data_ref', default=None)),
        ('url_repo_model', sgqlc.types.Arg(String, graphql_name='url_repo_model', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_pipeline_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addPipeline_products', default=None)),
        ('remove_pipeline_products', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removePipeline_products', default=None)),
        ('add_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAnnotations', default=None)),
        ('remove_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeAnnotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_pipeline_info_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePipeline_infoForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_pipeline_info_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validatePipeline_infoAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pipeline_infos_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='pipeline_infosZendroDefinition')
    products = sgqlc.types.Field(sgqlc.types.list_of('product'), graphql_name='products', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderProductInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_product = sgqlc.types.Field('product', graphql_name='readOneProduct', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_products = sgqlc.types.Field(Int, graphql_name='countProducts', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_product = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateProduct')
    products_connection = sgqlc.types.Field(ProductConnection, graphql_name='productsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderProductInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_product_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateProductForCreation', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('producer', sgqlc.types.Arg(String, graphql_name='producer', default=None)),
        ('project', sgqlc.types.Arg(String, graphql_name='project', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_file_assoc', sgqlc.types.Arg(ID, graphql_name='addFileAssoc', default=None)),
        ('add_pipeline', sgqlc.types.Arg(ID, graphql_name='addPipeline', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_product_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateProductForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('observation_type', sgqlc.types.Arg(String, graphql_name='observation_type', default=None)),
        ('producer', sgqlc.types.Arg(String, graphql_name='producer', default=None)),
        ('project', sgqlc.types.Arg(String, graphql_name='project', default=None)),
        ('metadata', sgqlc.types.Arg(JSON, graphql_name='metadata', default=None)),
        ('created_at', sgqlc.types.Arg(DateTime, graphql_name='createdAt', default=None)),
        ('updated_at', sgqlc.types.Arg(DateTime, graphql_name='updatedAt', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('add_file_assoc', sgqlc.types.Arg(ID, graphql_name='addFileAssoc', default=None)),
        ('remove_file_assoc', sgqlc.types.Arg(ID, graphql_name='removeFileAssoc', default=None)),
        ('add_pipeline', sgqlc.types.Arg(ID, graphql_name='addPipeline', default=None)),
        ('remove_pipeline', sgqlc.types.Arg(ID, graphql_name='removePipeline', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_product_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateProductForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_product_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateProductAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    products_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='productsZendroDefinition')
    roles = sgqlc.types.Field(sgqlc.types.list_of('role'), graphql_name='roles', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRoleInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderRoleInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_role = sgqlc.types.Field('role', graphql_name='readOneRole', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_roles = sgqlc.types.Field(Int, graphql_name='countRoles', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRoleInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_role = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateRole')
    roles_connection = sgqlc.types.Field('RoleConnection', graphql_name='rolesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRoleInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderRoleInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_role_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRoleForCreation', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_role_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRoleForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('add_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUsers', default=None)),
        ('remove_users', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUsers', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_role_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRoleForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_role_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRoleAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    roles_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='rolesZendroDefinition')
    role_to_users = sgqlc.types.Field(sgqlc.types.list_of('role_to_user'), graphql_name='role_to_users', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRole_to_userInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderRole_to_userInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_role_to_user = sgqlc.types.Field('role_to_user', graphql_name='readOneRole_to_user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_role_to_users = sgqlc.types.Field(Int, graphql_name='countRole_to_users', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRole_to_userInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_role_to_user = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateRole_to_user')
    role_to_users_connection = sgqlc.types.Field('Role_to_userConnection', graphql_name='role_to_usersConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRole_to_userInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderRole_to_userInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_role_to_user_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRole_to_userForCreation', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(Int, graphql_name='user_id', default=None)),
        ('role_id', sgqlc.types.Arg(Int, graphql_name='role_id', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_role_to_user_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRole_to_userForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('user_id', sgqlc.types.Arg(Int, graphql_name='user_id', default=None)),
        ('role_id', sgqlc.types.Arg(Int, graphql_name='role_id', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_role_to_user_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRole_to_userForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_role_to_user_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateRole_to_userAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    role_to_users_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='role_to_usersZendroDefinition')
    transects = sgqlc.types.Field(sgqlc.types.list_of('transect'), graphql_name='transects', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchTransectInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderTransectInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_transect = sgqlc.types.Field('transect', graphql_name='readOneTransect', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_transects = sgqlc.types.Field(Int, graphql_name='countTransects', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchTransectInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_transect = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateTransect')
    transects_connection = sgqlc.types.Field('TransectConnection', graphql_name='transectsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchTransectInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderTransectInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_transect_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateTransectForCreation', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('sum_vegetation_structure', sgqlc.types.Arg(Float, graphql_name='sum_vegetation_structure', default=None)),
        ('sum_indicator_species', sgqlc.types.Arg(Float, graphql_name='sum_indicator_species', default=None)),
        ('sum_impact', sgqlc.types.Arg(Float, graphql_name='sum_impact', default=None)),
        ('date_transecto', sgqlc.types.Arg(DateTime, graphql_name='date_transecto', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('percentage', sgqlc.types.Arg(Float, graphql_name='percentage', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_transect_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateTransectForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('sum_vegetation_structure', sgqlc.types.Arg(Float, graphql_name='sum_vegetation_structure', default=None)),
        ('sum_indicator_species', sgqlc.types.Arg(Float, graphql_name='sum_indicator_species', default=None)),
        ('sum_impact', sgqlc.types.Arg(Float, graphql_name='sum_impact', default=None)),
        ('date_transecto', sgqlc.types.Arg(DateTime, graphql_name='date_transecto', default=None)),
        ('latitude', sgqlc.types.Arg(Float, graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(Float, graphql_name='longitude', default=None)),
        ('percentage', sgqlc.types.Arg(Float, graphql_name='percentage', default=None)),
        ('add_associated_node', sgqlc.types.Arg(ID, graphql_name='addAssociated_node', default=None)),
        ('remove_associated_node', sgqlc.types.Arg(ID, graphql_name='removeAssociated_node', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_transect_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateTransectForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_transect_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateTransectAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    transects_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='transectsZendroDefinition')
    users = sgqlc.types.Field(sgqlc.types.list_of('user'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_user = sgqlc.types.Field('user', graphql_name='readOneUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_users = sgqlc.types.Field(Int, graphql_name='countUsers', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_user = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateUser')
    users_connection = sgqlc.types.Field('UserConnection', graphql_name='usersConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_user_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateUserForCreation', args=sgqlc.types.ArgDict((
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='is_active', default=None)),
        ('last_login', sgqlc.types.Arg(DateTime, graphql_name='last_login', default=None)),
        ('add_institutions', sgqlc.types.Arg(ID, graphql_name='addInstitutions', default=None)),
        ('add_roles', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addRoles', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_cumulus', default=None)),
        ('add_user_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUser_annotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_user_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateUserForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='first_name', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='last_name', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='is_active', default=None)),
        ('last_login', sgqlc.types.Arg(DateTime, graphql_name='last_login', default=None)),
        ('add_institutions', sgqlc.types.Arg(ID, graphql_name='addInstitutions', default=None)),
        ('remove_institutions', sgqlc.types.Arg(ID, graphql_name='removeInstitutions', default=None)),
        ('add_roles', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addRoles', default=None)),
        ('remove_roles', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeRoles', default=None)),
        ('add_associated_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addAssociated_cumulus', default=None)),
        ('remove_associated_cumulus', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeAssociated_cumulus', default=None)),
        ('add_user_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addUser_annotations', default=None)),
        ('remove_user_annotations', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeUser_annotations', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_user_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateUserForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_user_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateUserAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    users_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='usersZendroDefinition')
    visits = sgqlc.types.Field(sgqlc.types.list_of('visit'), graphql_name='visits', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderVisitInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    read_one_visit = sgqlc.types.Field('visit', graphql_name='readOneVisit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    count_visits = sgqlc.types.Field(Int, graphql_name='countVisits', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
))
    )
    csv_table_template_visit = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='csvTableTemplateVisit')
    visits_connection = sgqlc.types.Field('VisitConnection', graphql_name='visitsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderVisitInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    validate_visit_for_creation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateVisitForCreation', args=sgqlc.types.ArgDict((
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('date_sipecam_first_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_first_season', default=None)),
        ('date_sipecam_second_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_second_season', default=None)),
        ('date_first_season', sgqlc.types.Arg(Date, graphql_name='date_first_season', default=None)),
        ('date_second_season', sgqlc.types.Arg(Date, graphql_name='date_second_season', default=None)),
        ('report_first_season', sgqlc.types.Arg(String, graphql_name='report_first_season', default=None)),
        ('report_second_season', sgqlc.types.Arg(String, graphql_name='report_second_season', default=None)),
        ('add_cumulus_visit', sgqlc.types.Arg(ID, graphql_name='addCumulus_visit', default=None)),
        ('add_unique_node_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_node_pristine', default=None)),
        ('add_unique_node_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_node_disturbed', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_visit_for_updating = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateVisitForUpdating', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('comments', sgqlc.types.Arg(String, graphql_name='comments', default=None)),
        ('date_sipecam_first_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_first_season', default=None)),
        ('date_sipecam_second_season', sgqlc.types.Arg(Date, graphql_name='date_sipecam_second_season', default=None)),
        ('date_first_season', sgqlc.types.Arg(Date, graphql_name='date_first_season', default=None)),
        ('date_second_season', sgqlc.types.Arg(Date, graphql_name='date_second_season', default=None)),
        ('report_first_season', sgqlc.types.Arg(String, graphql_name='report_first_season', default=None)),
        ('report_second_season', sgqlc.types.Arg(String, graphql_name='report_second_season', default=None)),
        ('add_cumulus_visit', sgqlc.types.Arg(ID, graphql_name='addCumulus_visit', default=None)),
        ('remove_cumulus_visit', sgqlc.types.Arg(ID, graphql_name='removeCumulus_visit', default=None)),
        ('add_unique_node_pristine', sgqlc.types.Arg(ID, graphql_name='addUnique_node_pristine', default=None)),
        ('remove_unique_node_pristine', sgqlc.types.Arg(ID, graphql_name='removeUnique_node_pristine', default=None)),
        ('add_unique_node_disturbed', sgqlc.types.Arg(ID, graphql_name='addUnique_node_disturbed', default=None)),
        ('remove_unique_node_disturbed', sgqlc.types.Arg(ID, graphql_name='removeUnique_node_disturbed', default=None)),
        ('add_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='addMonitors', default=None)),
        ('remove_monitors', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='removeMonitors', default=None)),
        ('skip_associations_existence_checks', sgqlc.types.Arg(Boolean, graphql_name='skipAssociationsExistenceChecks', default=False)),
))
    )
    validate_visit_for_deletion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateVisitForDeletion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    validate_visit_after_reading = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateVisitAfterReading', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    visits_zendro_definition = sgqlc.types.Field(GraphQLJSONObject, graphql_name='visitsZendroDefinition')


class RoleConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'roles', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RoleEdge'), graphql_name='edges')
    roles = sgqlc.types.Field(sgqlc.types.list_of('role'), graphql_name='roles')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class RoleEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('role'), graphql_name='node')


class Role_to_userConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'role_to_users', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('Role_to_userEdge'), graphql_name='edges')
    role_to_users = sgqlc.types.Field(sgqlc.types.list_of('role_to_user'), graphql_name='role_to_users')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class Role_to_userEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('role_to_user'), graphql_name='node')


class TransectConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'transects', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('TransectEdge'), graphql_name='edges')
    transects = sgqlc.types.Field(sgqlc.types.list_of('transect'), graphql_name='transects')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class TransectEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('transect'), graphql_name='node')


class UserConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'users', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    users = sgqlc.types.Field(sgqlc.types.list_of('user'), graphql_name='users')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class UserEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('user'), graphql_name='node')


class VisitConnection(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('edges', 'visits', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.list_of('VisitEdge'), graphql_name='edges')
    visits = sgqlc.types.Field(sgqlc.types.list_of('visit'), graphql_name='visits')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('pageInfo'), graphql_name='pageInfo')


class VisitEdge(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('visit'), graphql_name='node')


class annotations_geom_obs_type(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'classified_by', 'classification_method', 'observation_type', 'confidence', 'geometry', 'video_frame_num', 'frequency_min', 'frequency_max', 'time_min', 'time_max', 'updated_at', 'created_at', 'file_id', 'user_id', 'pipeline_id', 'file_to', 'user_to', 'pipeline_annotation', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    classified_by = sgqlc.types.Field(String, graphql_name='classified_by')
    classification_method = sgqlc.types.Field(String, graphql_name='classification_method')
    observation_type = sgqlc.types.Field(String, graphql_name='observation_type')
    confidence = sgqlc.types.Field(Float, graphql_name='confidence')
    geometry = sgqlc.types.Field(GeoJSONGeometryCollectionScalar, graphql_name='geometry')
    video_frame_num = sgqlc.types.Field(Int, graphql_name='video_frame_num')
    frequency_min = sgqlc.types.Field(Float, graphql_name='frequency_min')
    frequency_max = sgqlc.types.Field(Float, graphql_name='frequency_max')
    time_min = sgqlc.types.Field(Float, graphql_name='time_min')
    time_max = sgqlc.types.Field(Float, graphql_name='time_max')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    file_id = sgqlc.types.Field(Int, graphql_name='file_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')
    pipeline_id = sgqlc.types.Field(Int, graphql_name='pipeline_id')
    file_to = sgqlc.types.Field('file', graphql_name='fileTo', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
))
    )
    user_to = sgqlc.types.Field('user', graphql_name='userTo', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
))
    )
    pipeline_annotation = sgqlc.types.Field('pipeline_info', graphql_name='pipeline_annotation', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPipeline_infoInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class calendar(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'date_started', 'date_finished', 'sipecam_year', 'order', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    date_started = sgqlc.types.Field(Date, graphql_name='date_started')
    date_finished = sgqlc.types.Field(Date, graphql_name='date_finished')
    sipecam_year = sgqlc.types.Field(String, graphql_name='sipecam_year')
    order = sgqlc.types.Field(Int, graphql_name='order')
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class cumulus(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'name', 'geometry', 'criteria_id', 'user_ids', 'ecosystem_id', 'con_socio', 'cumulus_criteria', 'unique_ecosystem', 'devices_filter', 'devices_connection', 'count_filtered_devices', 'associated_partners_filter', 'associated_partners_connection', 'count_filtered_associated_partners', 'visits_filter', 'visits_connection', 'count_filtered_visits', 'monitors_filter', 'monitors_connection', 'count_filtered_monitors', 'nodes_filter', 'nodes_connection', 'count_filtered_nodes', 'deployments_filter', 'deployments_connection', 'count_filtered_deployments', 'individuals_filter', 'individuals_connection', 'count_filtered_individuals', 'file_counts_filter', 'file_counts_connection', 'count_filtered_file_counts', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    geometry = sgqlc.types.Field(GeoJSONPolygonScalar, graphql_name='geometry')
    criteria_id = sgqlc.types.Field(Int, graphql_name='criteria_id')
    user_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='user_ids')
    ecosystem_id = sgqlc.types.Field(Int, graphql_name='ecosystem_id')
    con_socio = sgqlc.types.Field(Int, graphql_name='con_socio')
    cumulus_criteria = sgqlc.types.Field('cumulus_criteria', graphql_name='cumulus_criteria', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulus_criteriaInput, graphql_name='search', default=None)),
))
    )
    unique_ecosystem = sgqlc.types.Field('ecosystem', graphql_name='unique_ecosystem', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchEcosystemInput, graphql_name='search', default=None)),
))
    )
    devices_filter = sgqlc.types.Field(sgqlc.types.list_of('physical_device'), graphql_name='devicesFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPhysical_deviceInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    devices_connection = sgqlc.types.Field(Physical_deviceConnection, graphql_name='devicesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPhysical_deviceInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_devices = sgqlc.types.Field(Int, graphql_name='countFilteredDevices', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
))
    )
    associated_partners_filter = sgqlc.types.Field(sgqlc.types.list_of('user'), graphql_name='associated_partnersFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    associated_partners_connection = sgqlc.types.Field(UserConnection, graphql_name='associated_partnersConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_associated_partners = sgqlc.types.Field(Int, graphql_name='countFilteredAssociated_partners', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
))
    )
    visits_filter = sgqlc.types.Field(sgqlc.types.list_of('visit'), graphql_name='visitsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderVisitInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    visits_connection = sgqlc.types.Field(VisitConnection, graphql_name='visitsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderVisitInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_visits = sgqlc.types.Field(Int, graphql_name='countFilteredVisits', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
))
    )
    monitors_filter = sgqlc.types.Field(sgqlc.types.list_of('monitor'), graphql_name='monitorsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderMonitorInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    monitors_connection = sgqlc.types.Field(MonitorConnection, graphql_name='monitorsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderMonitorInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_monitors = sgqlc.types.Field(Int, graphql_name='countFilteredMonitors', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
))
    )
    nodes_filter = sgqlc.types.Field(sgqlc.types.list_of('node'), graphql_name='nodesFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderNodeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    nodes_connection = sgqlc.types.Field(NodeConnection, graphql_name='nodesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderNodeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_nodes = sgqlc.types.Field(Int, graphql_name='countFilteredNodes', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    deployments_filter = sgqlc.types.Field(sgqlc.types.list_of('deployment'), graphql_name='deploymentsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    deployments_connection = sgqlc.types.Field(DeploymentConnection, graphql_name='deploymentsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_deployments = sgqlc.types.Field(Int, graphql_name='countFilteredDeployments', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
))
    )
    individuals_filter = sgqlc.types.Field(sgqlc.types.list_of('individual'), graphql_name='individualsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderIndividualInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    individuals_connection = sgqlc.types.Field(IndividualConnection, graphql_name='individualsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderIndividualInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_individuals = sgqlc.types.Field(Int, graphql_name='countFilteredIndividuals', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
))
    )
    file_counts_filter = sgqlc.types.Field(sgqlc.types.list_of('file_count'), graphql_name='file_countsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFile_countInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFile_countInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    file_counts_connection = sgqlc.types.Field(File_countConnection, graphql_name='file_countsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFile_countInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFile_countInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_file_counts = sgqlc.types.Field(Int, graphql_name='countFilteredFile_counts', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFile_countInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class cumulus_criteria(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'name', 'cumulus_filter', 'cumulus_connection', 'count_filtered_cumulus', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    cumulus_filter = sgqlc.types.Field(sgqlc.types.list_of(cumulus), graphql_name='cumulusFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    cumulus_connection = sgqlc.types.Field(CumulusConnection, graphql_name='cumulusConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_cumulus = sgqlc.types.Field(Int, graphql_name='countFilteredCumulus', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class deployment(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'date_deployment', 'latitude', 'longitude', 'altitude', 'comments', 'metadata', 'kobo_url', 'device_id', 'node_id', 'cumulus_id', 'device', 'node', 'cumulus', 'files_filter', 'files_connection', 'count_filtered_files', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    date_deployment = sgqlc.types.Field(DateTime, graphql_name='date_deployment')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    altitude = sgqlc.types.Field(Float, graphql_name='altitude')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    metadata = sgqlc.types.Field(JSON, graphql_name='metadata')
    kobo_url = sgqlc.types.Field(String, graphql_name='kobo_url')
    device_id = sgqlc.types.Field(Int, graphql_name='device_id')
    node_id = sgqlc.types.Field(Int, graphql_name='node_id')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    device = sgqlc.types.Field('physical_device', graphql_name='device', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
))
    )
    node = sgqlc.types.Field('node', graphql_name='node', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    cumulus = sgqlc.types.Field('cumulus', graphql_name='cumulus', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    files_filter = sgqlc.types.Field(sgqlc.types.list_of('file'), graphql_name='filesFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFileInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    files_connection = sgqlc.types.Field(FileConnection, graphql_name='filesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderFileInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_files = sgqlc.types.Field(Int, graphql_name='countFilteredFiles', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class device_catalog(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'brand', 'type', 'physical_devices_filter', 'physical_devices_connection', 'count_filtered_physical_devices', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    type = sgqlc.types.Field(String, graphql_name='type')
    physical_devices_filter = sgqlc.types.Field(sgqlc.types.list_of('physical_device'), graphql_name='physical_devicesFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPhysical_deviceInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    physical_devices_connection = sgqlc.types.Field(Physical_deviceConnection, graphql_name='physical_devicesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderPhysical_deviceInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_physical_devices = sgqlc.types.Field(Int, graphql_name='countFilteredPhysical_devices', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPhysical_deviceInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class ecosystem(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'name', 'unique_node_filter', 'unique_node_connection', 'count_filtered_unique_node', 'cumulus_ecosystem_filter', 'cumulus_ecosystem_connection', 'count_filtered_cumulus_ecosystem', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    unique_node_filter = sgqlc.types.Field(sgqlc.types.list_of('node'), graphql_name='unique_nodeFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderNodeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    unique_node_connection = sgqlc.types.Field(NodeConnection, graphql_name='unique_nodeConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderNodeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_unique_node = sgqlc.types.Field(Int, graphql_name='countFilteredUnique_node', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    cumulus_ecosystem_filter = sgqlc.types.Field(sgqlc.types.list_of(cumulus), graphql_name='cumulus_ecosystemFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    cumulus_ecosystem_connection = sgqlc.types.Field(CumulusConnection, graphql_name='cumulus_ecosystemConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_cumulus_ecosystem = sgqlc.types.Field(Int, graphql_name='countFilteredCumulus_ecosystem', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class ecosystem_files(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'ecosystem', 'file_count_ecosystem')
    id = sgqlc.types.Field(ID, graphql_name='id')
    ecosystem = sgqlc.types.Field(String, graphql_name='ecosystem')
    file_count_ecosystem = sgqlc.types.Field(sgqlc.types.list_of('file_count_ecosystem'), graphql_name='file_count_ecosystem')


class file(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'url', 'date_deployment_device', 'type', 'id_alfresco', 'storage', 'updated_at', 'created_at', 'deployment_id', 'associated_deployment', 'file_annotations_filter', 'file_annotations_connection', 'count_filtered_file_annotations', 'file_products_filter', 'file_products_connection', 'count_filtered_file_products', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    url = sgqlc.types.Field(String, graphql_name='url')
    date_deployment_device = sgqlc.types.Field(Date, graphql_name='date_deployment_device')
    type = sgqlc.types.Field(String, graphql_name='type')
    id_alfresco = sgqlc.types.Field(String, graphql_name='id_alfresco')
    storage = sgqlc.types.Field(String, graphql_name='storage')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    deployment_id = sgqlc.types.Field(Int, graphql_name='deployment_id')
    associated_deployment = sgqlc.types.Field(deployment, graphql_name='associated_deployment', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
))
    )
    file_annotations_filter = sgqlc.types.Field(sgqlc.types.list_of(annotations_geom_obs_type), graphql_name='file_annotationsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    file_annotations_connection = sgqlc.types.Field(Annotations_geom_obs_typeConnection, graphql_name='file_annotationsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_file_annotations = sgqlc.types.Field(Int, graphql_name='countFilteredFile_annotations', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
))
    )
    file_products_filter = sgqlc.types.Field(sgqlc.types.list_of('product'), graphql_name='file_productsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderProductInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    file_products_connection = sgqlc.types.Field(ProductConnection, graphql_name='file_productsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderProductInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_file_products = sgqlc.types.Field(Int, graphql_name='countFilteredFile_products', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class file_count(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'delivery_date', 'audio_files', 'image_files', 'video_files', 'size', 'cumulus_id', 'cumulus_files', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    delivery_date = sgqlc.types.Field(Date, graphql_name='delivery_date')
    audio_files = sgqlc.types.Field(Int, graphql_name='audio_files')
    image_files = sgqlc.types.Field(Int, graphql_name='image_files')
    video_files = sgqlc.types.Field(Int, graphql_name='video_files')
    size = sgqlc.types.Field(Int, graphql_name='size')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    cumulus_files = sgqlc.types.Field(cumulus, graphql_name='cumulus_files', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class file_count_ecosystem(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'delivery_date', 'audio_files', 'image_files', 'video_files', 'size', 'cumulus_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(Int, graphql_name='id')
    delivery_date = sgqlc.types.Field(Date, graphql_name='delivery_date')
    audio_files = sgqlc.types.Field(Int, graphql_name='audio_files')
    image_files = sgqlc.types.Field(Int, graphql_name='image_files')
    video_files = sgqlc.types.Field(Int, graphql_name='video_files')
    size = sgqlc.types.Field(Int, graphql_name='size')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')


class individual(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'date_trap', 'latitude', 'longitude', 'altitude', 'comments', 'metadata', 'kobo_url', 'clave_posicion_malla', 'arete', 'node_id', 'cumulus_id', 'associated_node', 'associated_cumulus', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    date_trap = sgqlc.types.Field(DateTime, graphql_name='date_trap')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    altitude = sgqlc.types.Field(Float, graphql_name='altitude')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    metadata = sgqlc.types.Field(JSON, graphql_name='metadata')
    kobo_url = sgqlc.types.Field(String, graphql_name='kobo_url')
    clave_posicion_malla = sgqlc.types.Field(String, graphql_name='clave_posicion_malla')
    arete = sgqlc.types.Field(Int, graphql_name='arete')
    node_id = sgqlc.types.Field(Int, graphql_name='node_id')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    associated_node = sgqlc.types.Field('node', graphql_name='associated_node', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    associated_cumulus = sgqlc.types.Field(cumulus, graphql_name='associated_cumulus', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class institution(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'name', 'address', 'phone_number', 'users_filter', 'users_connection', 'count_filtered_users', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    address = sgqlc.types.Field(String, graphql_name='address')
    phone_number = sgqlc.types.Field(Int, graphql_name='phone_number')
    users_filter = sgqlc.types.Field(sgqlc.types.list_of('user'), graphql_name='usersFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    users_connection = sgqlc.types.Field(UserConnection, graphql_name='usersConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_users = sgqlc.types.Field(Int, graphql_name='countFilteredUsers', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class monitor(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'first_name', 'last_name', 'second_last_name', 'contact', 'cumulus_id', 'visit_ids', 'cumulus_monitor', 'visits_filter', 'visits_connection', 'count_filtered_visits', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    first_name = sgqlc.types.Field(String, graphql_name='first_name')
    last_name = sgqlc.types.Field(String, graphql_name='last_name')
    second_last_name = sgqlc.types.Field(String, graphql_name='second_last_name')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    visit_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='visit_ids')
    cumulus_monitor = sgqlc.types.Field(cumulus, graphql_name='cumulus_monitor', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    visits_filter = sgqlc.types.Field(sgqlc.types.list_of('visit'), graphql_name='visitsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderVisitInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    visits_connection = sgqlc.types.Field(VisitConnection, graphql_name='visitsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderVisitInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_visits = sgqlc.types.Field(Int, graphql_name='countFilteredVisits', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class node(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'nomenclatura', 'con_socio', 'fid', 'location', 'cat_integr', 'cumulus_id', 'ecosystem_id', 'cumulus_node', 'unique_visit_pristine', 'unique_visit_disturbed', 'ecosystems', 'deployments_filter', 'deployments_connection', 'count_filtered_deployments', 'individuals_filter', 'individuals_connection', 'count_filtered_individuals', 'transects_filter', 'transects_connection', 'count_filtered_transects', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    nomenclatura = sgqlc.types.Field(String, graphql_name='nomenclatura')
    con_socio = sgqlc.types.Field(Int, graphql_name='con_socio')
    fid = sgqlc.types.Field(Int, graphql_name='fid')
    location = sgqlc.types.Field(GeoJSONPointScalar, graphql_name='location')
    cat_integr = sgqlc.types.Field(String, graphql_name='cat_integr')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    ecosystem_id = sgqlc.types.Field(Int, graphql_name='ecosystem_id')
    cumulus_node = sgqlc.types.Field(cumulus, graphql_name='cumulus_node', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    unique_visit_pristine = sgqlc.types.Field('visit', graphql_name='unique_visit_pristine', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
))
    )
    unique_visit_disturbed = sgqlc.types.Field('visit', graphql_name='unique_visit_disturbed', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchVisitInput, graphql_name='search', default=None)),
))
    )
    ecosystems = sgqlc.types.Field(ecosystem, graphql_name='ecosystems', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchEcosystemInput, graphql_name='search', default=None)),
))
    )
    deployments_filter = sgqlc.types.Field(sgqlc.types.list_of(deployment), graphql_name='deploymentsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    deployments_connection = sgqlc.types.Field(DeploymentConnection, graphql_name='deploymentsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_deployments = sgqlc.types.Field(Int, graphql_name='countFilteredDeployments', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
))
    )
    individuals_filter = sgqlc.types.Field(sgqlc.types.list_of(individual), graphql_name='individualsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderIndividualInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    individuals_connection = sgqlc.types.Field(IndividualConnection, graphql_name='individualsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderIndividualInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_individuals = sgqlc.types.Field(Int, graphql_name='countFilteredIndividuals', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchIndividualInput, graphql_name='search', default=None)),
))
    )
    transects_filter = sgqlc.types.Field(sgqlc.types.list_of('transect'), graphql_name='transectsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchTransectInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderTransectInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    transects_connection = sgqlc.types.Field(TransectConnection, graphql_name='transectsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchTransectInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderTransectInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_transects = sgqlc.types.Field(Int, graphql_name='countFilteredTransects', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchTransectInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class pageInfo(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('start_cursor', 'end_cursor', 'has_previous_page', 'has_next_page')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')


class physical_device(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'serial_number', 'comments', 'status', 'previous_cumulus_ids', 'device_id', 'cumulus_id', 'device', 'cumulus_device', 'device_deployments_filter', 'device_deployments_connection', 'count_filtered_device_deployments', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    serial_number = sgqlc.types.Field(String, graphql_name='serial_number')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    status = sgqlc.types.Field(String, graphql_name='status')
    previous_cumulus_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='previous_cumulus_ids')
    device_id = sgqlc.types.Field(Int, graphql_name='device_id')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    device = sgqlc.types.Field(device_catalog, graphql_name='device', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDevice_catalogInput, graphql_name='search', default=None)),
))
    )
    cumulus_device = sgqlc.types.Field(cumulus, graphql_name='cumulus_device', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    device_deployments_filter = sgqlc.types.Field(sgqlc.types.list_of(deployment), graphql_name='device_deploymentsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    device_deployments_connection = sgqlc.types.Field(DeploymentConnection, graphql_name='device_deploymentsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderDeploymentInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_device_deployments = sgqlc.types.Field(Int, graphql_name='countFilteredDevice_deployments', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchDeploymentInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class pipeline_info(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'version', 'commit_dvc_of_data_ref', 'url_repo_model', 'updated_at', 'created_at', 'comments', 'pipeline_products_filter', 'pipeline_products_connection', 'count_filtered_pipeline_products', 'annotations_filter', 'annotations_connection', 'count_filtered_annotations', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    version = sgqlc.types.Field(String, graphql_name='version')
    commit_dvc_of_data_ref = sgqlc.types.Field(String, graphql_name='commit_dvc_of_data_ref')
    url_repo_model = sgqlc.types.Field(String, graphql_name='url_repo_model')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    pipeline_products_filter = sgqlc.types.Field(sgqlc.types.list_of('product'), graphql_name='pipeline_productsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderProductInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    pipeline_products_connection = sgqlc.types.Field(ProductConnection, graphql_name='pipeline_productsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderProductInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_pipeline_products = sgqlc.types.Field(Int, graphql_name='countFilteredPipeline_products', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchProductInput, graphql_name='search', default=None)),
))
    )
    annotations_filter = sgqlc.types.Field(sgqlc.types.list_of(annotations_geom_obs_type), graphql_name='annotationsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    annotations_connection = sgqlc.types.Field(Annotations_geom_obs_typeConnection, graphql_name='annotationsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_annotations = sgqlc.types.Field(Int, graphql_name='countFilteredAnnotations', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class product(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'type', 'url', 'observation_type', 'producer', 'project', 'metadata', 'created_at', 'updated_at', 'comments', 'pipeline_id', 'file_id', 'file_assoc', 'pipeline', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(String, graphql_name='type')
    url = sgqlc.types.Field(String, graphql_name='url')
    observation_type = sgqlc.types.Field(String, graphql_name='observation_type')
    producer = sgqlc.types.Field(String, graphql_name='producer')
    project = sgqlc.types.Field(String, graphql_name='project')
    metadata = sgqlc.types.Field(JSON, graphql_name='metadata')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    pipeline_id = sgqlc.types.Field(Int, graphql_name='pipeline_id')
    file_id = sgqlc.types.Field(Int, graphql_name='file_id')
    file_assoc = sgqlc.types.Field(file, graphql_name='fileAssoc', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchFileInput, graphql_name='search', default=None)),
))
    )
    pipeline = sgqlc.types.Field(pipeline_info, graphql_name='pipeline', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchPipeline_infoInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class role(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'name', 'description', 'users_filter', 'users_connection', 'count_filtered_users', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    users_filter = sgqlc.types.Field(sgqlc.types.list_of('user'), graphql_name='usersFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    users_connection = sgqlc.types.Field(UserConnection, graphql_name='usersConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderUserInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_users = sgqlc.types.Field(Int, graphql_name='countFilteredUsers', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchUserInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class role_to_user(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'user_id', 'role_id', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class transect(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'number', 'sum_vegetation_structure', 'sum_indicator_species', 'sum_impact', 'date_transecto', 'latitude', 'longitude', 'percentage', 'node_id', 'associated_node', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    number = sgqlc.types.Field(Int, graphql_name='number')
    sum_vegetation_structure = sgqlc.types.Field(Float, graphql_name='sum_vegetation_structure')
    sum_indicator_species = sgqlc.types.Field(Float, graphql_name='sum_indicator_species')
    sum_impact = sgqlc.types.Field(Float, graphql_name='sum_impact')
    date_transecto = sgqlc.types.Field(DateTime, graphql_name='date_transecto')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    percentage = sgqlc.types.Field(Float, graphql_name='percentage')
    node_id = sgqlc.types.Field(Int, graphql_name='node_id')
    associated_node = sgqlc.types.Field(node, graphql_name='associated_node', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class user(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'institution_id', 'cumulus_ids', 'institutions', 'roles_filter', 'roles_connection', 'count_filtered_roles', 'associated_cumulus_filter', 'associated_cumulus_connection', 'count_filtered_associated_cumulus', 'user_annotations_filter', 'user_annotations_connection', 'count_filtered_user_annotations', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    username = sgqlc.types.Field(String, graphql_name='username')
    password = sgqlc.types.Field(String, graphql_name='password')
    first_name = sgqlc.types.Field(String, graphql_name='first_name')
    last_name = sgqlc.types.Field(String, graphql_name='last_name')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')
    last_login = sgqlc.types.Field(DateTime, graphql_name='last_login')
    institution_id = sgqlc.types.Field(Int, graphql_name='institution_id')
    cumulus_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cumulus_ids')
    institutions = sgqlc.types.Field(institution, graphql_name='institutions', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchInstitutionInput, graphql_name='search', default=None)),
))
    )
    roles_filter = sgqlc.types.Field(sgqlc.types.list_of(role), graphql_name='rolesFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRoleInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderRoleInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    roles_connection = sgqlc.types.Field(RoleConnection, graphql_name='rolesConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRoleInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderRoleInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_roles = sgqlc.types.Field(Int, graphql_name='countFilteredRoles', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchRoleInput, graphql_name='search', default=None)),
))
    )
    associated_cumulus_filter = sgqlc.types.Field(sgqlc.types.list_of(cumulus), graphql_name='associated_cumulusFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    associated_cumulus_connection = sgqlc.types.Field(CumulusConnection, graphql_name='associated_cumulusConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderCumulusInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_associated_cumulus = sgqlc.types.Field(Int, graphql_name='countFilteredAssociated_cumulus', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    user_annotations_filter = sgqlc.types.Field(sgqlc.types.list_of(annotations_geom_obs_type), graphql_name='user_annotationsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    user_annotations_connection = sgqlc.types.Field(Annotations_geom_obs_typeConnection, graphql_name='user_annotationsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderAnnotations_geom_obs_typeInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_user_annotations = sgqlc.types.Field(Int, graphql_name='countFilteredUser_annotations', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchAnnotations_geom_obs_typeInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')


class visit(sgqlc.types.Type):
    __schema__ = sipecam_zendro_schema
    __field_names__ = ('id', 'comments', 'date_sipecam_first_season', 'date_sipecam_second_season', 'date_first_season', 'date_second_season', 'report_first_season', 'report_second_season', 'cumulus_id', 'pristine_id', 'disturbed_id', 'monitor_ids', 'cumulus_visit', 'unique_node_pristine', 'unique_node_disturbed', 'monitors_filter', 'monitors_connection', 'count_filtered_monitors', 'as_cursor')
    id = sgqlc.types.Field(ID, graphql_name='id')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    date_sipecam_first_season = sgqlc.types.Field(Date, graphql_name='date_sipecam_first_season')
    date_sipecam_second_season = sgqlc.types.Field(Date, graphql_name='date_sipecam_second_season')
    date_first_season = sgqlc.types.Field(Date, graphql_name='date_first_season')
    date_second_season = sgqlc.types.Field(Date, graphql_name='date_second_season')
    report_first_season = sgqlc.types.Field(String, graphql_name='report_first_season')
    report_second_season = sgqlc.types.Field(String, graphql_name='report_second_season')
    cumulus_id = sgqlc.types.Field(Int, graphql_name='cumulus_id')
    pristine_id = sgqlc.types.Field(Int, graphql_name='pristine_id')
    disturbed_id = sgqlc.types.Field(Int, graphql_name='disturbed_id')
    monitor_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='monitor_ids')
    cumulus_visit = sgqlc.types.Field(cumulus, graphql_name='cumulus_visit', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchCumulusInput, graphql_name='search', default=None)),
))
    )
    unique_node_pristine = sgqlc.types.Field(node, graphql_name='unique_node_pristine', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    unique_node_disturbed = sgqlc.types.Field(node, graphql_name='unique_node_disturbed', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchNodeInput, graphql_name='search', default=None)),
))
    )
    monitors_filter = sgqlc.types.Field(sgqlc.types.list_of(monitor), graphql_name='monitorsFilter', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderMonitorInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationInput), graphql_name='pagination', default=None)),
))
    )
    monitors_connection = sgqlc.types.Field(MonitorConnection, graphql_name='monitorsConnection', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
        ('order', sgqlc.types.Arg(sgqlc.types.list_of(orderMonitorInput), graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(paginationCursorInput), graphql_name='pagination', default=None)),
))
    )
    count_filtered_monitors = sgqlc.types.Field(Int, graphql_name='countFilteredMonitors', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(searchMonitorInput, graphql_name='search', default=None)),
))
    )
    as_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='asCursor')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
sipecam_zendro_schema.query_type = Query
sipecam_zendro_schema.mutation_type = Mutation
sipecam_zendro_schema.subscription_type = None

