import os
import argparse
import datetime
import pathlib
import shutil
from multiprocessing import Pool
import itertools

from simex import get_logger_for_writing_logs_to_file
from simex import SUFFIXES_SIPECAM, SUFFIXES_SIPECAM_AUDIO, \
SUFFIXES_SIPECAM_IMAGES, SUFFIXES_SIPECAM_VIDEO
from simex.utils.directories_and_files import multiple_file_types
from simex import read_metadata_image, read_metadata_audio

SUFFIXES_AUDIO_IMAGES = SUFFIXES_SIPECAM_AUDIO + SUFFIXES_SIPECAM_IMAGES

def extract_serial_number_of_file_and_move_if_necessary(tup):
    """
    Helper function to extract serial number of file.
    """
    filename, serial_number_ref = tup
    f_pathlib = pathlib.Path(filename)
    if f_pathlib.suffix in SUFFIXES_SIPECAM_AUDIO:
        dict_metadata_of_device = read_metadata_audio.get_metadata_of_device(filename)
    else:
        if f_pathlib.suffix in SUFFIXES_SIPECAM_IMAGES:
            dict_metadata_of_device = read_metadata_image.get_metadata_of_device(filename)
    serial_number_file = dict_metadata_of_device["SerialNumber"]
    if serial_number_ref is None:
        return serial_number_file
    else:
        if f_pathlib.suffix in SUFFIXES_SIPECAM_AUDIO or f_pathlib.suffix in SUFFIXES_SIPECAM_IMAGES:
            if not serial_number_file == serial_number_ref:
                dir_pathlib = f_pathlib.parent
                dir_diff_serial_number = os.path.join(dir_pathlib,
                                                      serial_number_file + \
                                                      "_new_dir")
                os.makedirs(dir_diff_serial_number, exist_ok=True)
                dst_f_diff_serial_number = os.path.join(dir_diff_serial_number,
                                                        f_pathlib.name)
                try:
                    f_pathlib.rename(dst_f_diff_serial_number)
                except:
                    shutil.move(filename, dst_f_diff_serial_number)
                return dir_diff_serial_number


def arguments_parse():
    help = """
Traverse files in a directory to check if audio files are empty

--------------
Example usage:
--------------

check_if_files_in_dir_are_from_different_serial_numbers_and_move_them --input_directory /dir/ --number_of_processes

If serial number is already known then it can be passed in the cli:
check_if_files_in_dir_are_from_different_serial_numbers_and_move_them --input_directory /dir/ --number_of_processes --serial_number_reference serial_number

"""


    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input_directory",
                        required=True,
                        default=None,
                        help="Directory with sipecam files")
    parser.add_argument("--serial_number_reference",
                        required=False,
                        default=None,
                        help="Directory with sipecam files")
    parser.add_argument("--number_of_processes",
                        required=True,
                        type=int,
                        default=None,
                        help="Select number of processes for parallel execution, if not parallel select 1")
    args = parser.parse_args()
    return args

def main():
    def extract_serial_number_of_reference(input_dir):
        iterator = multiple_file_types(input_dir,
                                       SUFFIXES_AUDIO_IMAGES)
        not_success = True
        while not_success:
            try:
                filename = next(iterator)
                logger.info("extraction of metadata of device from %s" % filename)
                serial_number_file = extract_serial_number_of_file_and_move_if_necessary((filename,None))
                if serial_number_file:
                    logger.info("SUCCESSFUL extraction of serial number of %s" % filename)
                    not_success = False
            except Exception as e:
                logger.info(e)
                logger.info("there were no audios nor images found in dir: %s, serial number can not be retrieved from " % input_dir)
                not_success = False
                serial_number_file = ""
        return serial_number_file
        
    
    args = arguments_parse()
    input_directory = args.input_directory
    serial_number_ref = args.serial_number_reference
    number_of_processes = args.number_of_processes
    filename_for_logs = "logs_simex_check_if_files_in_dir_are_from_different_serial_numbers_and_move_them"
    logger = get_logger_for_writing_logs_to_file(input_directory,
                                                 filename_for_logs)
    logger.info("check if there are files in dir from different serial numbers and move them")

    if not serial_number_ref:
        serial_number_ref = extract_serial_number_of_reference(input_directory)
    
    if serial_number_ref:
        iterator = multiple_file_types(input_directory,
                                       SUFFIXES_AUDIO_IMAGES)
        iterator_with_constant = zip(iterator, itertools.repeat(serial_number_ref))
        with Pool(processes=number_of_processes) as pool:
            list_map = pool.map(extract_serial_number_of_file_and_move_if_necessary,
                                iterator_with_constant)
        shared_volume = "/shared_volume"
        os.makedirs(shared_volume, exist_ok=True)
        list_for_new_dirs_created = os.path.join(shared_volume,
                                             "simex_new_dirs_created_because_of_sampling_errors_" + \
                                             datetime.date.today().strftime("%d-%m-%Y") + \
                                             ".txt")
        list_for_files_moved_because_errors = os.path.join(shared_volume,
                                                           "simex_files_moved_because_of_sampling_errors_" + \
                                                           datetime.date.today().strftime("%d-%m-%Y") + \
                                                           ".txt")
        aux_list_for_new_dirs = []
        with open(list_for_new_dirs_created, "a") as dst_file_for_new_dirs:
            for directory in list_map:
                if directory is not None and directory not in aux_list_for_new_dirs:
                    logger.info("Dir: %s had files with different serial numbers", directory)
                    dst_file_for_new_dirs.write(directory + "\n")
                    aux_list_for_new_dirs.append(directory)
                    with open(list_for_files_moved_because_errors, 'a') as dst_file_for_files_because_errors:
                       for f in multiple_file_types(directory, SUFFIXES_SIPECAM):
                           dst_file_for_files_because_errors.write(f + "\n")
