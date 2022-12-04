import os
import argparse
import datetime
import pathlib
from multiprocessing import Pool
import subprocess

from simex import get_logger_for_writing_logs_to_file
from simex import SUFFIXES_SIPECAM_AUDIO
from simex.utils.directories_and_files import multiple_file_types

def check_audio_file(filename):
    """
    Helper function to check if audio file when reading it with exiftool
    either one of next sentences are in the metadata:
    "Error": "Entire file is binary zeros"
    Recording cancelled before completion due to change of switch position.
    "Error": "File is empty"
    Is outside main to execute it in parallel.
    """
    f_pathlib = pathlib.Path(filename)
    cmd = "".join(["exiftool -a -j ", "\"", filename, "\""])
    run_out_cmd = subprocess.run(cmd,
                                 shell=True,
                                 capture_output=True)
    run_out_cmd_stdout_empty = run_out_cmd.stdout.find(b"empty")
    run_out_cmd_stdout_cancelled = run_out_cmd.stdout.find(b"cancelled")
    run_out_cmd_stdout_binary_zeros = run_out_cmd.stdout.find(b"binary zeros")
    run_out_cmd_file_format_error = run_out_cmd.stdout.find(b"format error")
    run_out_cmd_stdout_binary_zeros_ffs = run_out_cmd.stdout.find(b"binary 0xff's")
    if run_out_cmd_stdout_empty != -1 or run_out_cmd_stdout_cancelled != -1 or run_out_cmd_stdout_binary_zeros != -1 or run_out_cmd_file_format_error != -1 or run_out_cmd_stdout_binary_zeros_ffs != -1:
        dir_pathlib = f_pathlib.parent
        dir_error = os.path.join(dir_pathlib,
                                 "error")
        os.makedirs(dir_error, exist_ok=True)
        dst_f_error = os.path.join(dir_error,
                                   f_pathlib.name)
        f_pathlib.rename(dst_f_error)
        return dir_error


def arguments_parse():
    help = """
Traverse files in a directory to check if audio files are empty

--------------
Example usage:
--------------

check_if_there_are_audio_empty_files_in_dir_and_move_them --input_directory_audio /dir/ --number_of_processes

"""


    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input_directory_audio",
                        required=True,
                        default=None,
                        help="Directory with WAV files")
    parser.add_argument("--number_of_processes",
                        required=True,
                        type=int,
                        default=None,
                        help="Select number of processes for parallel execution, if not parallel select 1")
    args = parser.parse_args()
    return args

def main():
    args = arguments_parse()
    input_directory = args.input_directory_audio
    number_of_processes = args.number_of_processes
    filename_for_logs = "logs_simex_check_if_there_are_audio_empty_files_in_dir_and_move_them"
    logger = get_logger_for_writing_logs_to_file(input_directory,
                                                 filename_for_logs)
    logger.info("check if there are audio empty files in dir and move them")

    iterator = multiple_file_types(input_directory,
                                   SUFFIXES_SIPECAM_AUDIO)

    with Pool(processes=number_of_processes) as pool:
        list_map = pool.map(check_audio_file,
                            iterator)
        shared_volume = "/shared_volume"
        os.makedirs(shared_volume, exist_ok=True)
        list_for_new_dirs_created = os.path.join(shared_volume,
                                             "simex_new_dirs_created_because_of_sampling_errors_" + \
                                             datetime.date.today().strftime("%d-%m-%Y") + \
                                             ".txt")
        with open(list_for_new_dirs_created, "a") as file:
            for elem in list_map:
                file.write(elem + "\n")
