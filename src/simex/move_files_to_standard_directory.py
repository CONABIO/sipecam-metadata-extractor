import os
import argparse
import json
import pathlib
import datetime
import shutil
import hashlib
import re

from shapely.geometry import Point, Polygon
from simex import get_logger_for_writing_logs_to_file
from simex.utils.zendro import query_for_move_files_to_standard_directory, \
query_alternative_auxiliar_for_move_files_to_standard_directory, \
query_alternative_for_move_files_to_standard_directory
from simex.utils.directories_and_files import multiple_file_types
from simex import SUFFIXES_SIPECAM_AUDIO, SUFFIXES_SIPECAM_IMAGES, SUFFIXES_SIPECAM_VIDEO, \
SUFFIXES_SIPECAM

SUFFIXES_SIPECAM_IMAGES_VIDEO = SUFFIXES_SIPECAM_IMAGES + SUFFIXES_SIPECAM_VIDEO

def build_polygon_for_cumulus_geometry(cumulus_geom_coordinates):
    """
    Retrieve Polygon geometry using coordinates list of cumulus.
    """
    geom = []
    for point in cumulus_geom_coordinates:
        geom.append((point[1],point[0]))
    poly = Polygon(geom)
    return poly

def check_if_point_is_in_cumulus_geom(lat,lng, poly):
    """
    Validate if point is in Polygon geometry of cumulus.
    """
    try:
        point_to_check = Point(lat,lng)
        if point_to_check.within(poly.buffer(0.2)):
            return (lat, lng)
        else:
            return None
    except:
        return None

def fill_metadata_of_device_with_query_results(d_source,
                                               nom_node,
                                               cumulus_name,
                                               lat_centroid_cumulus,
                                               long_centroid_cumulus,
                                               date_deploy,
                                               ecosystems_name,
                                               latitude_device,
                                               longitude_device,
                                               node_cat_integrity):
    """
    Fill MetadataDevice key of dictionary d_source with results of
    query to tables of Zendro.
    """
    dict_output_metadatadevice                             = d_source["MetadataDevice"].copy()
    dict_output_metadatadevice["NomenclatureNode"]         = nom_node
    dict_output_metadatadevice["CumulusName"]              = cumulus_name
    dict_output_metadatadevice["CentroidCumulusLatitude"]  = lat_centroid_cumulus
    dict_output_metadatadevice["CentroidCumulusLongitude"] = long_centroid_cumulus
    dict_output_metadatadevice["DateDeployment"]           = date_deploy
    dict_output_metadatadevice["EcosystemsName"]           = ecosystems_name
    dict_output_metadatadevice["Latitude"]                 = latitude_device
    dict_output_metadatadevice["Longitude"]                = longitude_device
    dict_output_metadatadevice["NodeCategoryIntegrity"]    = node_cat_integrity
    return dict_output_metadatadevice

def get_output_dict_std_dir_and_json_file(dst_dir,
                                          d_source,
                                          d_output_metadatadevice,
                                          type_files_in_dir,
                                          dry_run):
    """
    Returns dictionary that will be used to fill json file, also will be returned and
    standard directory where files will be moved.
    Args:
        dry_run (bool): if true then don't move anything
    """
    dict_output_metadata  = {}
    dict_output_metadata["DaysBetweenFirstAndLastDate"] = d_source["DaysBetweenFirstAndLastDate"]
    dict_output_metadata["MetadataDevice"]              = d_output_metadatadevice
    if type_files_in_dir == "audios":
        filename_key = next(iter(d_source["MetadataFiles"]))
        sample_rate = d_source["MetadataFiles"][filename_key]["SampleRate"]
        if sample_rate == 384000:
            type_audio = "Ultrasonico"
        else:
            if sample_rate == 48000:
                type_audio = "Audible"
            else:
                type_audio = "Audible_Ultrasonico"
        standard_dir = os.path.join(dst_dir,
                                    type_files_in_dir,
                                    type_audio
                                    )
    else:
        if type_files_in_dir == "images" or type_files_in_dir == "videos":
            standard_dir = os.path.join(dst_dir,
                                        "images_videos")

    standard_dir_pathlib = pathlib.Path(standard_dir)
    if not dry_run:
        os.makedirs(standard_dir, exist_ok=True)
    file_with_metadata_updated = os.path.join(standard_dir,
                                              standard_dir_pathlib.name + \
                                              "_simex_metadata_files_and_device_" + \
                                              datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + \
                                              ".json")
    dict_output_metadata["MetadataFiles"] = {}

    return (dict_output_metadata,
            standard_dir,
            file_with_metadata_updated)

def md5_for_file(path, block_size=256*128):
    """
    Block size directly depends on the block size of your filesystem
    to avoid performances issues
    Here I have blocks of 4096 octets (Default NTFS)
    See:
    https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
    """
    md5 = hashlib.md5()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
             md5.update(chunk)
    return md5.hexdigest()

def get_fields_from_device_deploymentsFilter_query_result(device_deploymentsFilter_list):
    """
    Retrieve results of query to Zendro in variables.
    """
    device_deploymentsFilter_dict = device_deploymentsFilter_list[0]
    nomenclature_node     = device_deploymentsFilter_dict["node"]["nomenclatura"]
    cumulus_name          = device_deploymentsFilter_dict["cumulus"]["name"]
    cumulus_geometry      = device_deploymentsFilter_dict["cumulus"]["geometry"]
    date_of_deployment    = device_deploymentsFilter_dict["date_deployment"].split('T')[0]
    ecosystems_name       = device_deploymentsFilter_dict["node"]["ecosystems"]["name"]
    latitude_device       = device_deploymentsFilter_dict["latitude"]
    longitude_device      = device_deploymentsFilter_dict["longitude"]
    node_cat_integrity    = device_deploymentsFilter_dict["node"]["cat_integr"]
    return (nomenclature_node,
            cumulus_name,
            cumulus_geometry,
            date_of_deployment,
            ecosystems_name,
            latitude_device,
            longitude_device,
            node_cat_integrity)

def get_latref_long_ref(latitude, longitude):
    """
    Build dictionary with GPSLatitudeRef & GPSLongitudeRef
    in case are missing for images & videos files.
    """
    try:
        return {"GPSLatitudeRef": "North" if latitude >= 0 else "South",
                "GPSLongitudeRef": "East" if longitude >= 0 else "West"
                }
    except:
        return {"GPSLatitudeRef": "",
                "GPSLongitudeRef": ""
                }

def assign_gps_info_of_device_to_metadata_of_images_and_videos(logger,
                                                               d_metadatafiles_for_file,
                                                               d_output_metadatadevice):
    """
    If there is no GPS information in files metadata then use device metadata extracted from
    Zendro Deployment table to fill it.
    """
    if not d_metadatafiles_for_file["GPSLatitudeRef"]:
        logger.info("GPS info of files werent available, using the ones of device to fill them")
        lat  = d_output_metadatadevice["Latitude"]
        long = d_output_metadatadevice["Longitude"]
        d_latlong_ref = get_latref_long_ref(lat, long)
        d_metadatafiles_for_file["GPSLatitudeRef"]  = d_latlong_ref["GPSLatitudeRef"]
        d_metadatafiles_for_file["GPSLongitudeRef"] = d_latlong_ref["GPSLongitudeRef"]
        d_metadatafiles_for_file["GPSLatitude"]     = lat
        d_metadatafiles_for_file["GPSLongitude"]    = long

def extend_metadata_of_audios(d_metadatafiles_for_file,
                             d_output_metadatadevice):
    """
    Fill latitude, longitude for audio files with info of latitude, longitude of
    device.
    """
    lat  = d_output_metadatadevice["Latitude"]
    long = d_output_metadatadevice["Longitude"]
    d_metadatafiles_for_file["Latitude"] = lat
    d_metadatafiles_for_file["Longitude"] = long

def check_files_coords_and_assign_them_to_device_if_necessary(logger,
                                                              lat_file,
                                                              long_file,
                                                              cumulus_poly,
                                                              d_metadatadevice,
                                                              d_metadatafiles_for_file,
                                                              type_files_in_dir
                                                              ):
    """
    For a given file check if coordinates of it fall in cumulus polygon.
    Also check coordinates of device, if don't fall in cumulus polygon then use the ones from the files.
    """
    t_lat_long_file = check_if_point_is_in_cumulus_geom(lat_file,
                                                        long_file,
                                                        cumulus_poly)
    if t_lat_long_file:
        logger.info("Latitude and Longitude of file are in cumulus geometry")
        lat_file  = t_lat_long_file[0]
        long_file = t_lat_long_file[1]
        #check if lat long of device are None and use lat long of file to fill them
        if not d_metadatadevice["Latitude"] and not d_metadatadevice["Longitude"]:
            logger.info("Using lat long of file to fill lat long of device")
            d_metadatadevice["Latitude"]  = lat_file
            d_metadatadevice["Longitude"] = long_file
    else:
        logger.info("Latitude and Longitude of file are not in cumulus geometry, returning None")
        logger.info("Using lat long of device to fill lat long of file")
        #if lat long of file are None then use lat long of device.
        lat_file  = d_metadatadevice["Latitude"]
        long_file = d_metadatadevice["Longitude"]
    if type_files_in_dir == "images" or type_files_in_dir == "videos":
        d_metadatafiles_for_file["GPSLatitude"]  = lat_file
        d_metadatafiles_for_file["GPSLongitude"] = long_file
    else:
        if type_files_in_dir == "audios":
            d_metadatafiles_for_file["Latitude"]  = lat_file
            d_metadatafiles_for_file["Longitude"] = long_file

def register_dir_that_couldnt_move(fname_source_first_date_pathlib,
                                   move_files,
                                   path_for_std_directory,
                                   src_dir):
    """
    Auxiliar function to register directory src_dir that couldn't move to path_for_std_directory
    Args:
        fname_source_first_date_pathlib (instance of pathlib class): help to find suffix of filename
        move_files (boolean):            wether to move files if conditions in main function are met. Expected false
        path_for_std_directory (str):    path where files were going to moved
        src_dir (str):                   directory that have source files and json file with serial number and dates.
    """
    #register which dirs couldn't be moved
    create_txt_of_dirs_not_moved = False
    if fname_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM and not move_files:
        create_txt_of_dirs_not_moved = True
    if create_txt_of_dirs_not_moved:
        name_dir_for_dirs_not_moved  = "dirs_not_moved_with_simex"
        path_for_dir_with_txt_of_dirs_not_moved  = os.path.join(path_for_std_directory,
                                                                name_dir_for_dirs_not_moved)
        os.makedirs(path_for_dir_with_txt_of_dirs_not_moved,  exist_ok=True)
        path_for_txt_with_dirs_not_moved  = os.path.join(path_for_dir_with_txt_of_dirs_not_moved,
                                                         name_dir_for_dirs_not_moved) + "_" + \
                                                         datetime.date.today().strftime("%d-%m-%Y") + \
                                                         ".txt"
        with open(path_for_txt_with_dirs_not_moved, "a") as write_dst_dirs_not_moved:
            write_dst_dirs_not_moved.write(src_dir + "\n")

def return_files_moved_to_their_source_dir(d_mapping_dst_filename_src_filename,
                                           src_dir):
    """
    d_mapping_dst_filename_src_filename (dict): dictionary with key dst_filename which is the filename in
                                                standard_directory already moved and value src_filename
                                                which is the filename in source.
    src_dir (str): directory that have source files and json file with serial number and dates.
    """
    for dst_f, src_f in d_mapping_dst_filename_src_filename.items():
        dst_f_pathlib = pathlib.Path(dst_f)
        try:
            dst_f_pathlib.rename(src_f)
        except:
            shutil.move(src_f, dst_f)

def check_file_existence_in_standard_dir(logger,
                                         std_dir,
                                         src_dir,
                                         SUFFIXES,
                                         dst_f,
                                         d_mapping_dst_f_src_f,
                                         f_number,
                                         type_f_in_dir,
                                         dry_run):
    """
    Args:
        std_dir (str):                standard directory where will be checked if dst_f exists in there
        src_dir (str):                directory that have source files and json file with serial number and dates.
        SUFFIXES (list):              suffixes that will be used with dst_f to check if exists in std_dir
        dst_f (str):                  destiny filename in std_dir
        d_mapping_dst_f_src_f (dict): dictionary with key dst_filename which is the filename in
                                      standard_directory already moved and value src_filename
                                      which is the filename in source.
        f_number (str):               for images and videos this string is a sequence of numbers, e.g. 0001
        type_f_in_dir (str):          either one of: audios, images or videos string.
        dry_run (bool):               if true then don't move anything
    Returns:
        dst_filename_exists (boolean):wether dst_f exists in std_dir
    """
    #next variable to verify existence of files in standard_dir
    dst_filename_exists = False
    dst_filename_pathlib = pathlib.Path(dst_f)
    dst_filename_no_suffix = dst_f.split(dst_filename_pathlib.suffix)[0]
    for suffix in SUFFIXES:
        filename_to_test_if_exists = dst_filename_no_suffix + suffix
        filename_to_test_if_exists_pathlib = pathlib.Path(filename_to_test_if_exists)
        if filename_to_test_if_exists_pathlib.is_file():
            logger.info("File %s already exists in %s" %(dst_f, std_dir))
            dst_filename_exists = True
            if not dry_run:
                logger.info("Performing rollback, returning all files to their source dir")
                return_files_moved_to_their_source_dir(d_mapping_dst_f_src_f,
                                                       src_dir)
            logger.info("halting loop of checking if file exists")
            break
        else:
            if type_f_in_dir == "images" or type_f_in_dir == "videos":
                filename_number_to_test_existence = "*" + f_number + suffix
                pattern_test_existence            = [filename_number_to_test_existence]
                iterator_test_existence           = multiple_file_types(std_dir,
                                                                        pattern_test_existence)
                list_test_existence               = list(iterator_test_existence)
                if len(list_test_existence) > 0: #there's a image or video with same number in standard_dir
                    logger.info("Filenumber of file %s already exists in %s" %(dst_f,
                                                                               std_dir))
                    dst_filename_exists = True
                    if not dry_run:
                        logger.info("Performing rollback, returning all files to their source dir")
                        return_files_moved_to_their_source_dir(d_mapping_dst_f_src_f,
                                                               src_dir)
                    logger.info("halting loop of checking if file exists")
                    break
                else:
                    logger.info("File %s doesn't exists in %s, continuing with move cli" %(filename_to_test_if_exists,
                                                                                         std_dir))
            else:
                logger.info("File %s doesn't exists in %s, continuing with move cli" %(filename_to_test_if_exists,
                                                                                     std_dir))
    return dst_filename_exists


def move_files_to_standard_dir(logger,
                               path_for_std_dir,
                               src_dir,
                               dst_dir,
                               d_source,
                               d_output_metadatadevice,
                               cumulus_poly,
                               type_files_in_dir,
                               dry_run):
    """
    Move files from source directory to destiny directory, both given in standard input of this cli (move_files).
    Will be used for filling d_source.
    Args:
        path_for_std_dir (str):         auxiliar path that will be used to build standard_dir (what will be
                                        returned with this function).
        src_dir (str):                  directory that have source files and json file with serial number and dates.
        dst_dir (str):                  will hold standard directory.
                                        Prepends already built (cumulus name, nomenclature of node,
                                        date of deployment for example).
                                        Specifications of standard dir are built (if audio then use Ultrasonico or
                                        Audible names for instance) in this function.
        d_source (dict):                dictionary with info from extract cli simex (executed in a
                                        previous step before this cli).
        d_output_metadatadevice (dict): dictionary with device metadata info which has info from extract cli
                                        simex (executed in a previous step before this cli) and Zendro info
                                        extracted in this cli (move_files).
        cumulus_poly (geom shapely):    Polygon shapely of cumulus to check wether coordinates are in the cumulus.
        type_files_in_dir (str):        either one of: audios, images or videos string.
        dry_run (bool):                 if true then don't move anything
    Returns:
        standard_dir (str):             path where files are moved
    """
    #next dict will be build in case we want to do a rollback
    dict_mapping_dst_filename_src_filename = {}
    #get important variables for moving files
    dict_output_metadata, standard_dir, output_filename = get_output_dict_std_dir_and_json_file(dst_dir,
                                                                                                d_source,
                                                                                                d_output_metadatadevice,
                                                                                                type_files_in_dir,
                                                                                                dry_run)
    lat_centroid_cumulus  = dict_output_metadata["MetadataDevice"]["CentroidCumulusLatitude"]
    long_centroid_cumulus = dict_output_metadata["MetadataDevice"]["CentroidCumulusLongitude"]
    #create dir that will hold new dirs & files moved to standar_dir. Will be a txt file and it's name will
    #have the day when new dirs & files were moved.
    name_dir_for_new_dirs_moved  = "dirs_moved_with_simex"
    path_for_dir_with_txt_of_new_dirs_moved  = os.path.join(path_for_std_dir,
                                                            name_dir_for_new_dirs_moved)
    if not dry_run:
        os.makedirs(path_for_dir_with_txt_of_new_dirs_moved,  exist_ok=True)
    name_dir_for_new_files_moved = "files_moved_with_simex"
    path_for_dir_with_txt_of_new_files_moved = os.path.join(path_for_std_dir,
                                                            name_dir_for_new_files_moved)
    if not dry_run:
        os.makedirs(path_for_dir_with_txt_of_new_files_moved, exist_ok=True)
    path_for_txt_with_new_files_moved = os.path.join(path_for_dir_with_txt_of_new_files_moved,
                                                     name_dir_for_new_files_moved) + "_" + \
                                                     datetime.date.today().strftime("%d-%m-%Y") + \
                                                     ".txt"
    iterator = multiple_file_types(src_dir,
                                   SUFFIXES_SIPECAM)
    for filename in iterator:
        f_pathlib = pathlib.Path(filename)
        f_pathlib_suffix = f_pathlib.suffix
        filename_md5 = md5_for_file(filename) #md5 will be basename of filename
        if f_pathlib_suffix in SUFFIXES_SIPECAM_AUDIO:
            filename_number = None
            filename_std = "".join([filename_md5,
                                    f_pathlib_suffix])
            logger.info("File %s will be moved to: %s with name %s" % (filename, standard_dir,
                                                                       filename_std)
                       )
        else:
            if f_pathlib_suffix in SUFFIXES_SIPECAM_IMAGES_VIDEO:
                filename_number = re.findall("([0-9]{1,}).[JPG|AVI]", f_pathlib.name)[0] #get 0074 of RCNX0074.JPG
                filename_std = "".join([filename_md5,
                                        "_",
                                        filename_number,
                                        f_pathlib_suffix])
                logger.info("File %s will be moved to: %s with name %s" % (filename, standard_dir,
                                                                           filename_std)
                           )
        dst_filename = os.path.join(standard_dir, filename_std)
        #check if if exists dst_filename, if so, do a rollback and halt the program
        if f_pathlib_suffix in SUFFIXES_SIPECAM_AUDIO:
            SUFFIXES_TO_CHECK_EXISTENCE_OF_FILE = SUFFIXES_SIPECAM_AUDIO
        else:
            if f_pathlib_suffix in SUFFIXES_SIPECAM_IMAGES_VIDEO:
                SUFFIXES_TO_CHECK_EXISTENCE_OF_FILE = SUFFIXES_SIPECAM_IMAGES_VIDEO
        dst_filename_exists = check_file_existence_in_standard_dir(logger,
                                                                   standard_dir,
                                                                   src_dir,
                                                                   SUFFIXES_TO_CHECK_EXISTENCE_OF_FILE,
                                                                   dst_filename,
                                                                   dict_mapping_dst_filename_src_filename,
                                                                   filename_number,
                                                                   type_files_in_dir,
                                                                   dry_run)
        if dst_filename_exists:
            logger.info("halting loop of moving files")
            break
        if not dst_filename_exists:
            dict_mapping_dst_filename_src_filename[dst_filename] = filename
            #fill dict_output_metadata["MetadataFiles"] with d_source["MetadataFiles"]
            dict_output_metadata["MetadataFiles"][dst_filename] = d_source["MetadataFiles"][filename]
            if type_files_in_dir == "images" or type_files_in_dir == "videos":
                assign_gps_info_of_device_to_metadata_of_images_and_videos(logger,
                                                                           dict_output_metadata["MetadataFiles"][dst_filename],
                                                                           d_output_metadatadevice)
            else:
                if type_files_in_dir == "audios":
                    extend_metadata_of_audios(dict_output_metadata["MetadataFiles"][dst_filename],
                                              d_output_metadatadevice)
            if type_files_in_dir == "images" or type_files_in_dir == "videos":
                lat_file  = dict_output_metadata["MetadataFiles"][dst_filename]["GPSLatitude"]
                long_file = dict_output_metadata["MetadataFiles"][dst_filename]["GPSLongitude"]
            else:
                if type_files_in_dir == "audios":
                    lat_file  = dict_output_metadata["MetadataFiles"][dst_filename]["Latitude"]
                    long_file = dict_output_metadata["MetadataFiles"][dst_filename]["Longitude"]
            logger.info("Validating lat and long of file are correct using lat long of cumulus centroid")
            check_files_coords_and_assign_them_to_device_if_necessary(logger,
                                                                      lat_file,
                                                                      long_file,
                                                                      cumulus_poly,
                                                                      dict_output_metadata["MetadataDevice"],
                                                                      dict_output_metadata["MetadataFiles"][dst_filename],
                                                                      type_files_in_dir
                                                                      )
            logger.info("Writing lat long of centroid of cumulus for MetadataFiles")
            dict_output_metadata["MetadataFiles"][dst_filename]["CentroidCumulusLatitude"]  = lat_centroid_cumulus
            dict_output_metadata["MetadataFiles"][dst_filename]["CentroidCumulusLongitude"] = long_centroid_cumulus
            if not dry_run:
                try:
                    f_pathlib.rename(dst_filename) #move
                except:
                    shutil.move(filename, dst_filename)

    if not dst_filename_exists and not dry_run:
        path_for_txt_with_new_dirs_moved  = os.path.join(path_for_dir_with_txt_of_new_dirs_moved,
                                                         name_dir_for_new_dirs_moved) + "_" + \
                                                         datetime.date.today().strftime("%d-%m-%Y") + \
                                                         ".txt"
        #write standard_dir in txt
        with open(path_for_txt_with_new_dirs_moved, "a") as write_dst_new_dirs:
            write_dst_new_dirs.write(standard_dir + "\n")
        #write standard path for each file in txt
        with open(path_for_txt_with_new_files_moved, "a") as write_dst_new_files:
            for dst_f, src_f in dict_mapping_dst_filename_src_filename.items():
                write_dst_new_files.write(dst_f + "\n")
        #write json with metadata info for all files
        with open(output_filename, "w") as write_dst:
            json.dump(dict_output_metadata, write_dst)
    else:
        standard_dir = ""
    return standard_dir


def arguments_parse():
    help = """
Move files to directory of server. Path that will have the files is created
according to:
cumulus_name/node_nomenclature/date_of_device_deployment/type_of_device/uuid.(JPG|WAV|AVI)

--------------
Example usage:
--------------

move_files_to_standard_directory --directory_with_file_of_serial_number_and_dates /dir/ --path_for_standard_directory /data/

"""
    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--directory_with_file_of_serial_number_and_dates",
                        required=True,
                        default=None,
                        help="Directory that has json file with serial number and dates")
    parser.add_argument("--path_for_standard_directory",
                        required=True,
                        default=None,
                        help="Standard directory that will have files moved")
    parser.add_argument('--dry_run',
                        action='store_true',
                        help="Just show which files will going to be moved but don't do it")
    args = parser.parse_args()
    return args


def main():
    args = arguments_parse()
    directory_with_file_of_serial_number_and_dates = args.directory_with_file_of_serial_number_and_dates
    path_for_standard_directory = args.path_for_standard_directory
    dry_run = args.dry_run
    filename_for_logs = "logs_simex_move_files_to_standard_directory_" + \
                        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    logger = get_logger_for_writing_logs_to_file(directory_with_file_of_serial_number_and_dates,
                                                 filename_for_logs)
    input_directory_purepath = pathlib.PurePath(directory_with_file_of_serial_number_and_dates).name
    file_with_serial_number_and_dates = os.path.join(directory_with_file_of_serial_number_and_dates,
                                                     input_directory_purepath) + \
                                                     "_simex_extract_serial_numbers_dates_and_metadata_of_files_and_device.json"
    if dry_run:
        logger.info("Running in dry_run mode, will not move any files, just show cli functionality")
    with open(file_with_serial_number_and_dates, 'r') as f:
        dict_source = json.load(f)

    serial_number = dict_source["MetadataDevice"]["SerialNumber"]
    dict_source_dates = dict_source["FirstAndLastDate"] #dict_source_dates is a dictionary
    diff_dates = dict_source["DaysBetweenFirstAndLastDate"]

    logger.info("Dir %s has serial number %s" % (directory_with_file_of_serial_number_and_dates,
                                                 serial_number))
    try:
        tup_source_dates = tuple(dict_source_dates.items())
        filename_source_first_date,  first_date_str  = tup_source_dates[0]
        filename_source_second_date, second_date_str = tup_source_dates[1]
        logger.info("File %s has date %s" % (filename_source_first_date,
                                             first_date_str))
        logger.info("File %s has date %s" % (filename_source_second_date,
                                             second_date_str))
    except Exception as e:
        logger.info(e)
        logger.info("couldn't retrieve second_date_str possibly related to only one file taken by device")
        tup_source_dates = tuple(dict_source_dates.items())
        filename_source_first_date,  list_dates_str  = tup_source_dates[0]
        first_date_str  = list_dates_str[0]
        second_date_str = list_dates_str[1]
        logger.info("File %s has date %s" % (filename_source_first_date,
                                             first_date_str))
        logger.info("File %s only was taken in one date and date %s will be used for query" % (filename_source_first_date,
                                                                                               second_date_str))

    logger.info("DaysBetweenFirstAndLastDate: %s" % diff_dates)

    filename_source_first_date_pathlib = pathlib.Path(filename_source_first_date)
    MIN_NUMBER_OF_DAYS = 2
    MAX_NUMBER_OF_DAYS = 60
    #there were a lot of problems for images or videos that had DaysBetweenFirstAndLastDate 0 or 1 as there were erronous files
    #only files with DaysBetweenFirstAndLastDate >=2 will be incorporated into data standard dir.
    #there were a lot of problems for audios that had DaysBetweenFirstAndLastDate>= 60
    if diff_dates >= MIN_NUMBER_OF_DAYS and diff_dates <= MAX_NUMBER_OF_DAYS:
        move_files = True
    else:
        move_files = False
        query_result          = None
        operation_sgqlc       = None
        logger.info("There were images or videos in %s dir that have DaysBetweenFirstAndLastDate < %s or DaysBetweenFirstAndLastDate > %s, will not be moved" % (directory_with_file_of_serial_number_and_dates, MIN_NUMBER_OF_DAYS, MAX_NUMBER_OF_DAYS))

    #make query assuming first_date_str is less than date of deployment of device
    if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_AUDIO and move_files:
        type_files_in_dir = "audios"
        query_result, operation_sgqlc = query_for_move_files_to_standard_directory(serial_number,
                                                                                   first_date_str,
                                                                                   second_date_str,
                                                                                   file_type="audio")
    else:
        if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_IMAGES and move_files:
            type_files_in_dir = "images"
            query_result, operation_sgqlc = query_for_move_files_to_standard_directory(serial_number,
                                                                                       first_date_str,
                                                                                       second_date_str,
                                                                                       file_type="image")
        else:
            if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_VIDEO and move_files:
                type_files_in_dir = "videos"
                query_result, operation_sgqlc = query_for_move_files_to_standard_directory(serial_number,
                                                                                           first_date_str,
                                                                                           second_date_str,
                                                                                           file_type="video")
    logger.info("Query to Zendro GQL: %s" % operation_sgqlc)

    try:
        device_deploymentsFilter_list = query_result["data"]["physical_devices"][0]["device_deploymentsFilter"]
        if len(device_deploymentsFilter_list) == 1:
            tuple_result = get_fields_from_device_deploymentsFilter_query_result(device_deploymentsFilter_list)
            nomenclature_node, cumulus_name, cumulus_geometry, date_of_deployment, ecosystems_name, lat_device, long_device, node_cat_integrity = tuple_result
            logger.info("SUCCESSFUL extraction of nomenclature of node, cumulus name and date of deployment")
            logger.info("directory %s has nom node: %s, cum name: %s, date of depl: %s, ecosystems name: %s, \
                         latitude and longitude of device:  %s, %s, node category of integrity: %s" % \
                        (directory_with_file_of_serial_number_and_dates,
                         nomenclature_node,
                         cumulus_name,
                         date_of_deployment,
                         ecosystems_name,
                         lat_device,
                         long_device,
                         node_cat_integrity)
                       )
            logger.info("compute centroid of cumulus")
            cumulus_geom_coordinates = cumulus_geometry["coordinates"][0]
            cumulus_poly = build_polygon_for_cumulus_geometry(cumulus_geom_coordinates)
            lat_centroid_cumulus  = round(cumulus_poly.centroid.x, 5)
            long_centroid_cumulus = round(cumulus_poly.centroid.y, 5)
            logger.info("Centroid of cumulus, lat: %s, long: %s" %(lat_centroid_cumulus,
                                                                   long_centroid_cumulus))
            logger.info("Validating lat and long of device are correct using lat long of cumulus centroid")
            t_lat_long_device = check_if_point_is_in_cumulus_geom(lat_device,
                                                                  long_device,
                                                                  cumulus_poly)
            if t_lat_long_device:
                logger.info("Latitude and Longitude of device are in cumulus geometry")
                lat_device  = t_lat_long_device[0]
                long_device = t_lat_long_device[1]
            else:
                logger.info("Latitude and Longitude of device are not in cumulus geometry, returning None")
                lat_device  = None
                long_device = None
            logger.info("filling dict MetadataDevice using query results from Zendro")
            dict_output_metadatadevice = fill_metadata_of_device_with_query_results(dict_source,
                                                                                    nomenclature_node,
                                                                                    cumulus_name,
                                                                                    lat_centroid_cumulus,
                                                                                    long_centroid_cumulus,
                                                                                    date_of_deployment,
                                                                                    ecosystems_name,
                                                                                    lat_device,
                                                                                    long_device,
                                                                                    node_cat_integrity)
            path_for_files_moved = os.path.join(path_for_standard_directory,
                                                cumulus_name,
                                                nomenclature_node,
                                                serial_number,
                                                date_of_deployment)
            logger.info("path where files will be moved: %s" % path_for_files_moved)
            standard_directory = move_files_to_standard_dir(logger,
                                                            path_for_standard_directory,
                                                            directory_with_file_of_serial_number_and_dates,
                                                            path_for_files_moved,
                                                            dict_source,
                                                            dict_output_metadatadevice,
                                                            cumulus_poly,
                                                            type_files_in_dir,
                                                            dry_run)
            if not standard_directory:
                if not dry_run:
                    logger.info("registering dir that couldnt be moved: %s" % directory_with_file_of_serial_number_and_dates)
                    register_dir_that_couldnt_move(filename_source_first_date_pathlib,
                                                   move_files,
                                                   path_for_standard_directory,
                                                   directory_with_file_of_serial_number_and_dates)
            else:
                if not dry_run:
                    logger.info("copying logs of move cli to %s", standard_directory)
                    path_filename_for_logs = os.path.join(directory_with_file_of_serial_number_and_dates,
                                                      filename_for_logs + ".logs")
                    shutil.copy(path_filename_for_logs , standard_directory)
        else:
            if len(device_deploymentsFilter_list) == 0: #make another query as first_date_str could be greater than date of deployment of device
                logger.info("last query wasn't successful")
                if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_AUDIO and move_files:
                    query_result, operation_sgqlc = query_alternative_auxiliar_for_move_files_to_standard_directory(serial_number,
                                                                                                                    file_type="audio")
                else:
                    if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_IMAGES and move_files:
                        query_result, operation_sgqlc = query_alternative_auxiliar_for_move_files_to_standard_directory(serial_number,
                                                                                                                        file_type="image")
                    else:
                        if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_VIDEO and move_files:
                            query_result, operation_sgqlc = query_alternative_auxiliar_for_move_files_to_standard_directory(serial_number,
                                                                                                                            file_type="video")
                logger.info("Query alternative auxiliar to Zendro GQL: %s" % operation_sgqlc)
                logger.info("Result of query alternative auxiliar to Zendro GQL: %s" % query_result)
                try:
                    deployment_date_of_device_found = False #assume there is no interval of deployment dates registered in Zendro Deployment table that contains dates of files
                    device_deploymentsFilter_list = query_result["data"]["physical_devices"][0]["device_deploymentsFilter"]
                    format_string_data = "%Y-%m-%d"
                    list_dates_device_deployment = [d["date_deployment"].split('T')[0] for d in device_deploymentsFilter_list]
                    list_datetimes_device_deployment = [datetime.datetime.strptime(d["date_deployment"].split('T')[0],
                                                                                   format_string_data) for d in device_deploymentsFilter_list]
                    first_datetime  = datetime.datetime.strptime(first_date_str, format_string_data)
                    second_datetime = datetime.datetime.strptime(second_date_str, format_string_data)
                    list_datetimes_device_deployment.sort()
                    def get_date_of_device_deploymentsFilter_list(d):
                        return datetime.datetime.strptime(d["date_deployment"].split('T')[0],
                                                          format_string_data)
                    device_deploymentsFilter_list.sort(key=get_date_of_device_deploymentsFilter_list)

                    for k in range(len(list_datetimes_device_deployment) - 1):
                        datetime_device_deployment_1 = list_datetimes_device_deployment[k]
                        datetime_device_deployment_2 = list_datetimes_device_deployment[k+1]
                        diff_datetimes = second_datetime - datetime_device_deployment_1
                        diff_datetimes_days = diff_datetimes.days
                        if datetime_device_deployment_1 <= first_datetime and second_datetime <= datetime_device_deployment_2 and diff_datetimes_days <= MAX_NUMBER_OF_DAYS:
                            idx_date = k
                            break
                        else:
                            idx_date = None

                    if idx_date is None:
                        deployment_date_of_device_found = False
                        logger.info("there was no interval of deployment dates registered in Zendro Deployment table that contains dates of files")
                    else:
                        deployment_date_of_device_found = True

                    date_for_filter = device_deploymentsFilter_list[idx_date]["date_deployment"]

                    if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_AUDIO and move_files:
                        query_result, operation_sgqlc = query_alternative_for_move_files_to_standard_directory(serial_number,
                                                                                                               date_for_filter,
                                                                                                               file_type="audio")
                    else:
                        if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_IMAGES and move_files:
                            query_result, operation_sgqlc = query_alternative_for_move_files_to_standard_directory(serial_number,
                                                                                                                    date_for_filter,
                                                                                                                    file_type="image")
                        else:
                            if filename_source_first_date_pathlib.suffix in SUFFIXES_SIPECAM_VIDEO and move_files:
                                query_result, operation_sgqlc = query_alternative_for_move_files_to_standard_directory(serial_number,
                                                                                                                       date_for_filter,
                                                                                                                       file_type="video")
                    logger.info("Query alternative to Zendro GQL: %s" % operation_sgqlc)
                    try:
                        device_deploymentsFilter_list = query_result["data"]["physical_devices"][0]["device_deploymentsFilter"]
                        if len(device_deploymentsFilter_list) == 1:
                            tuple_result = get_fields_from_device_deploymentsFilter_query_result(device_deploymentsFilter_list)
                            nomenclature_node, cumulus_name, cumulus_geometry, date_of_deployment, ecosystems_name, lat_device, long_device, node_cat_integrity = tuple_result
                            logger.info("SUCCESSFUL extraction of nomenclature of node, cumulus name and date of deployment")
                            logger.info("directory %s has nom node: %s, cum name: %s, date of depl: %s, ecosystems name: %s, \
                                         latitude and longitude of device:  %s, %s, node category of integrity: %s" % \
                                        (directory_with_file_of_serial_number_and_dates,
                                         nomenclature_node,
                                         cumulus_name,
                                         date_of_deployment,
                                         ecosystems_name,
                                         lat_device,
                                         long_device,
                                         node_cat_integrity)
                                       )
                            logger.info("compute centroid of cumulus")
                            cumulus_geom_coordinates = cumulus_geometry["coordinates"][0]
                            cumulus_poly = build_polygon_for_cumulus_geometry(cumulus_geom_coordinates)
                            lat_centroid_cumulus  = round(cumulus_poly.centroid.x, 5)
                            long_centroid_cumulus = round(cumulus_poly.centroid.y, 5)
                            logger.info("Centroid of cumulus, lat: %s, long: %s" %(lat_centroid_cumulus,
                                                                                   long_centroid_cumulus))
                            logger.info("Validating lat and long of device are correct using lat long of cumulus centroid")
                            t_lat_long_device = check_if_point_is_in_cumulus_geom(lat_device,
                                                                                  long_device,
                                                                                  cumulus_poly)
                            if t_lat_long_device:
                                logger.info("Latitude and Longitude of device are in cumulus geometry")
                                lat_device  = t_lat_long_device[0]
                                long_device = t_lat_long_device[1]
                            else:
                                logger.info("Latitude and Longitude of device are not in cumulus geometry, returning None")
                                lat_device  = None
                                long_device = None
                            logger.info("filling dict MetadataDevice using query results from Zendro")
                            dict_output_metadatadevice = fill_metadata_of_device_with_query_results(dict_source,
                                                                                                    nomenclature_node,
                                                                                                    cumulus_name,
                                                                                                    lat_centroid_cumulus,
                                                                                                    long_centroid_cumulus,
                                                                                                    date_of_deployment,
                                                                                                    ecosystems_name,
                                                                                                    lat_device,
                                                                                                    long_device,
                                                                                                    node_cat_integrity)
                            path_for_files_moved = os.path.join(path_for_standard_directory,
                                                                cumulus_name,
                                                                nomenclature_node,
                                                                serial_number,
                                                                date_of_deployment)
                            logger.info("path where files will be moved: %s" % path_for_files_moved)
                            standard_directory = move_files_to_standard_dir(logger,
                                                                            path_for_standard_directory,
                                                                            directory_with_file_of_serial_number_and_dates,
                                                                            path_for_files_moved,
                                                                            dict_source,
                                                                            dict_output_metadatadevice,
                                                                            cumulus_poly,
                                                                            type_files_in_dir,
                                                                            dry_run)
                            if not standard_directory:
                                if not dry_run:
                                    logger.info("registering dir that couldnt be moved: %s" % directory_with_file_of_serial_number_and_dates)
                                    register_dir_that_couldnt_move(filename_source_first_date_pathlib,
                                                                   move_files,
                                                                   path_for_standard_directory,
                                                                   directory_with_file_of_serial_number_and_dates)
                            else:
                                if not dry_run:
                                    logger.info("copying logs of move cli to %s", standard_directory)
                                    path_filename_for_logs = os.path.join(directory_with_file_of_serial_number_and_dates,
                                                                      filename_for_logs + ".logs")
                                    shutil.copy(path_filename_for_logs , standard_directory)
                    except Exception as e:
                        logger.info(e)
                        logger.info("unsuccessful query %s or error when moving files to standard dir" % operation_sgqlc)
                        if not dry_run:
                            logger.info("registering dir that couldnt be moved: %s" % directory_with_file_of_serial_number_and_dates)
                            register_dir_that_couldnt_move(filename_source_first_date_pathlib,
                                                           move_files,
                                                           path_for_standard_directory,
                                                           directory_with_file_of_serial_number_and_dates)
                except Exception as e:
                    logger.info(e)
                    logger.info("unsuccessful query %s or error when moving files to standard dir" % operation_sgqlc)
                    if not dry_run:
                        logger.info("registering dir that couldnt be moved: %s" % directory_with_file_of_serial_number_and_dates)
                        register_dir_that_couldnt_move(filename_source_first_date_pathlib,
                                                       move_files,
                                                       path_for_standard_directory,
                                                       directory_with_file_of_serial_number_and_dates)
            else: #len of list is >1 then there's no unique date of deployment of device
                logger.info("There's no unique date of deployment and can not select one date to create standard directory")
                if not dry_run:
                    logger.info("registering dir that couldnt be moved: %s" % directory_with_file_of_serial_number_and_dates)
                    register_dir_that_couldnt_move(filename_source_first_date_pathlib,
                                                   move_files,
                                                   path_for_standard_directory,
                                                   directory_with_file_of_serial_number_and_dates)
    except Exception as e:
        logger.info(e)
        logger.info("unsuccessful query %s or error when moving files to standard dir" % operation_sgqlc)
        logger.info("Result of query to Zendro GQL: %s" % query_result)
        if not dry_run:
            logger.info("registering dir that couldnt be moved: %s" % directory_with_file_of_serial_number_and_dates)
            register_dir_that_couldnt_move(filename_source_first_date_pathlib,
                                           move_files,
                                           path_for_standard_directory,
                                           directory_with_file_of_serial_number_and_dates)
