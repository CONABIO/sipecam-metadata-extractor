import os
import datetime
import argparse

from simex import SUFFIXES_SIPECAM
from simex.utils.directories_and_files import multiple_file_types


def arguments_parse():
    help = """
Given a directory with SiPeCaM files, produce list of files whose metadata
will be extracted and list of directories where data will be copied
(traditional server).
--------------
Example usage:
--------------

list_of_files_and_subdirectories_to_extract_metadata --input_directory /input_dir

"""


    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input_directory",
                        required=True,
                        default=None,
                        help="Directory with data: audio, image and video")
    args = parser.parse_args()
    return args

def main():
    args = arguments_parse()
    input_directory = args.input_directory
    shared_volume = "/shared_volume"
    os.makedirs(shared_volume, exist_ok=True)
    sipecam_subdirectories = os.path.join(shared_volume,
                                          "sipecam_subdirectories_" + \
                                          datetime.date.today().strftime("%d-%m-%Y") + \
                                          ".txt")
    sipecam_files_to_extract_metadata = os.path.join(shared_volume,
                                        "sipecam_files_to_extract_metadata_from_" + \
                                        datetime.date.today().strftime("%d-%m-%Y") + \
                                        ".txt")

    list_of_subdirectories = []

    with open(sipecam_files_to_extract_metadata, "w+") as file:
        with open(sipecam_subdirectories, "w+") as subdirectory:
            for f in multiple_file_types(input_directory, SUFFIXES_SIPECAM,
                                         recursive=True):
                file.write(f + "\n")
                dirname_f = os.path.dirname(f)
                if dirname_f not in list_of_subdirectories:
                    subdirectory.write(dirname_f + "\n")
                    list_of_subdirectories.append(dirname_f)

