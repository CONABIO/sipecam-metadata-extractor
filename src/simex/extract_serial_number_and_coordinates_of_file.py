import glob
import os
import argparse
import json
import pathlib

from simex import get_logger_for_writing_logs_to_file
from simex import SUFFIXES_SIPECAM_AUDIO, SUFFIXES_SIPECAM_IMAGES
from simex.utils.directories_and_files import multiple_file_types
from simex import read_metadata_image, read_metadata_audio

SUFFIXES_TARGET = SUFFIXES_SIPECAM_AUDIO + SUFFIXES_SIPECAM_IMAGES

def arguments_parse():
    help = """
Traverse files in adirectory to extract serial number and coordinates of them.

--------------
Example usage:
--------------

extract_serial_numbers_and_coordinates --input_dir /dir/

"""


    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input_directory",
                        required=True,
                        default=None,
                        help="Directory with WAV, JPG, AVI files")
    args = parser.parse_args()
    return args

def main():
    args = arguments_parse()
    input_directory = args.input_directory
    dir_logs = "logs_simex_extract_serial_numbers_and_coordinates"
    logger = get_logger_for_writing_logs_to_file(input_directory,
                                                 dir_logs)    
    dirname_input_directory = os.path.dirname(input_directory)
    output_filename = os.path.join(input_directory,
                                   dirname_input_directory + \
                                   "_simex_extract_serial_numbers_and_coordinates.json")
    logger.info("extraction of serial number and coordinates")
    logger.info("logs in %s" % output_filename)
    
    #pathlib.Path(output_filename).unlink(missing_ok=True) #remove in case it exists
    dict_output = {} 
    
    def extract_serial_number(filename, type_filename):
        logger.info("extraction of serial number of %s" % filename)
        if type_filename == "audio":
            serial_number = read_metadata_audio.extract_serial_number(filename)
        else:
            if type_filename == "image":
                serial_number = read_metadata_image.extract_serial_number(filename)
        if not serial_number:
            logger.info("FAILED extraction of serial number of file")
            logger.info("returning empty serial number")
        return {filename: serial_number}
        
    with open(output_filename, "w") as dst:
        dict_output["SerialNumber"] = {}
        dict_output["Coordinates"] = {}
        
        for f in multiple_file_types(input_directory, 
                                     *SUFFIXES_TARGET):
            f_pathlib = pathlib.Path(f)
            if f_pathlib.suffix in SUFFIXES_SIPECAM_AUDIO:
                dict_serial_number = extract_serial_number(f, "audio")
            if f_pathlib.suffix in SUFFIXES_SIPECAM_IMAGES:
                dict_serial_number = extract_serial_number(f, "image")
            if dict_serial_number[filename]:
                dict_output["SerialNumber"].update(dict_serial_number)       
        json.dump(dict_output, dst)    
    

        
    