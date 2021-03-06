import os
import re
import argparse
import pathlib
import json
import datetime

from simex import SUFFIXES_SIPECAM_IMAGES, SUFFIXES_SIPECAM_VIDEO
from simex import get_logger_for_writing_logs_to_file
from simex.utils.directories_and_files import multiple_file_types
from simex import read_metadata_video

def arguments_parse():
    help = """
Traverse files in a directory to extend metadata of video files

--------------
Example usage:
--------------

extend_metadata_of_video_files --input_directory_video /dir/

"""


    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input_directory_video",
                        required=True,
                        default=None,
                        help="Directory with AVI files")
    args = parser.parse_args()
    return args

def main():
    args = arguments_parse()
    input_directory = args.input_directory_video
    filename_for_logs = "logs_simex_extend_metadata_of_video_files_2"
    logger = get_logger_for_writing_logs_to_file(input_directory,
                                                 filename_for_logs)
    input_directory_name = pathlib.Path(input_directory).name
    pattern = ["[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9].json"]#for json filename which includes date in "%d-%m-%Y" format
    iterator = multiple_file_types(input_directory, pattern)
    list_json_files = []
    for json_file in iterator:
        json_file_pathlib = pathlib.Path(json_file)
        json_filename = str(json_file_pathlib.name)
        list_json_files.append(json_filename)

    date_format = "%d-%m-%Y"
    list_datetimes_of_json_files = [datetime.datetime.strptime(re.findall("[0-9]{2}-[0-9]{2}-[0-9]{4}", s)[0],
                                                               date_format) for s in list_json_files]
    list_datetimes_of_json_files.sort()
    list_dates_json_files_sorted = [d.strftime(date_format) for d in list_datetimes_of_json_files]
    last_date = list_dates_json_files_sorted[len(list_dates_json_files_sorted)-1]
    file_with_video_metadata_source =os.path.join(input_directory,
                                                  input_directory_name + \
                                                  "_simex_metadata_files_and_device_" + \
                                                  last_date + \
                                                  ".json")
    logger.info("Json file that will be the source: %s" % file_with_video_metadata_source)

    with open(file_with_video_metadata_source, 'r') as f:
        dict_source = json.load(f)
    serial_number     = dict_source["MetadataDevice"]["SerialNumber"]
    centroid_cum_lat  = dict_source["MetadataDevice"]["CentroidCumulusLatitude"]
    centroid_cum_long = dict_source["MetadataDevice"]["CentroidCumulusLongitude"]
    
    for filename, metadata_file in dict_source["MetadataFiles"].items():
        filename_pathlib = pathlib.Path(filename)
        if filename_pathlib.suffix in SUFFIXES_SIPECAM_IMAGES:
            gps_latitude_ref  = dict_source["MetadataFiles"][filename]["GPSLatitudeRef"]
            gps_longitude_ref = dict_source["MetadataFiles"][filename]["GPSLongitudeRef"]
            gps_latitude      = dict_source["MetadataFiles"][filename]["GPSLatitude"]
            gps_longitude     = dict_source["MetadataFiles"][filename]["GPSLongitude"]
            break
    
    with open("/LUSTRE/sacmod/SIPECAM/videos_without_metadata_92.txt", 'r') as txt:
        list_with_files_to_extract_video_metadata = txt.read().splitlines()
    
    for filename in list_with_files_to_extract_video_metadata:
        metadata_file = read_metadata_video.get_metadata_of_file(filename)
        dict_source["MetadataFiles"][filename] = metadata_file
        dict_source["MetadataFiles"][filename]["SerialNumber"]             = serial_number
        dict_source["MetadataFiles"][filename]["CentroidCumulusLatitude"]  = centroid_cum_lat
        dict_source["MetadataFiles"][filename]["CentroidCumulusLongitude"] = centroid_cum_long
        dict_source["MetadataFiles"][filename]["GPSLatitudeRef"]           = gps_latitude_ref
        dict_source["MetadataFiles"][filename]["GPSLongitudeRef"]          = gps_longitude_ref
        dict_source["MetadataFiles"][filename]["GPSLatitude"]              = gps_latitude
        dict_source["MetadataFiles"][filename]["GPSLongitude"]             = gps_longitude
          

    file_with_video_metadata_dst = os.path.join(input_directory,
                                                input_directory_name) + \
                                                "_simex_metadata_files_and_device_" + \
                                                datetime.date.today().strftime(date_format) + \
                                                ".json"
    pathlib.Path(file_with_video_metadata_dst).unlink(missing_ok=True) #remove in case it exists
    with open(file_with_video_metadata_dst, 'w') as dst:
        json.dump(dict_source, dst)
