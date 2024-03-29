from setuptools import setup, find_packages

cli_list = "list_of_files_and_subdirectories_to_extract_metadata = simex.list_of_files_and_subdirectories_to_extract_metadata:main"
cli_extract_sn_d_md = "extract_serial_numbers_dates_and_metadata_of_files_and_device = simex.extract_serial_numbers_dates_and_metadata_of_files_and_device:main"
cli_generate_sipecam_zendro_schema = "generate_sipecam_zendro_schema = simex.generate_sipecam_zendro_schema:main"
cli_move_files_to_standard_directory = "move_files_to_standard_directory = simex.move_files_to_standard_directory:main"
cli_check_if_there_are_audio_empty_files_in_dir_and_move_them = "check_if_there_are_audio_empty_files_in_dir_and_move_them = simex.check_if_there_are_audio_empty_files_in_dir_and_move_them:main"
cli_extend_metadata_of_audio_files = "extend_metadata_of_audio_files = simex.extend_metadata_of_audio_files:main"
cli_extend_metadata_of_files = "extend_metadata_of_files = simex.extend_metadata_of_files:main"
cli_extend_metadata_of_video_files = "extend_metadata_of_video_files = simex.extend_metadata_of_video_files:main"
cli_check_if_files_in_dir_are_from_different_serial_numbers_and_move_them = "check_if_files_in_dir_are_from_different_serial_numbers_and_move_them = simex.check_if_files_in_dir_are_from_different_serial_numbers_and_move_them:main"

setup(name="simex", version=0.1,
      description=u"Simplify extraction of metadata for SiPeCaM files",
      author="CONABIO",
      packages=find_packages(),
      install_requires = ["python-dotenv==0.19.2",
                          "sgqlc==15.0",
                          "hachoir==3.1.2",
                          "PyExifTool==0.4.13",
                          "shapely==1.8.2"
                          ],
      entry_points = {
          'console_scripts': [
                              cli_list,
                              cli_extract_sn_d_md,
                              cli_generate_sipecam_zendro_schema,
                              cli_move_files_to_standard_directory,
                              cli_check_if_there_are_audio_empty_files_in_dir_and_move_them,
                              cli_extend_metadata_of_audio_files,
                              cli_extend_metadata_of_files,
                              cli_extend_metadata_of_video_files,
                              cli_check_if_files_in_dir_are_from_different_serial_numbers_and_move_them
                              ]
                     }
      )
