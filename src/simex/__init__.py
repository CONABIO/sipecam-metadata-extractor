import logging
import os
import pathlib

def setup_logging(logs_filename):
    """
    Function that will open file to hold log of file processed.
    Args:
        logs_filename (str): empty file name, will hold logs.
    Returns:
        logger: instance of logging, commonly named RootLogger.
    """
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
    file_handler = logging.FileHandler(logs_filename, mode='a')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logFormatter)
    logger = logging.getLogger()
    logger.setLevel(file_handler.level)
    logger.addHandler(file_handler)
    return logger

def get_logger_for_writing_logs_to_file(input_file, temp_dirname):
    """
    Helper function to setup logging to level specified
    in setup_logging function.
    Args:
        input_file (str): basename of file that will be processed.
        It's used for creating file with logs.
        temp_dirname (str): name of directory that will hold logs files.
    Returns:
        getLogger instance from logging module.
    """
    dirname_file = os.path.join(os.path.dirname(input_file),
                                temp_dirname)
    os.makedirs(dirname_file, exist_ok=True)
    logs_filename = os.path.join(dirname_file, "logs_" + \
                                 pathlib.Path(input_file).stem + ".txt") #trail extension
    pathlib.Path(logs_filename).unlink(missing_ok=True) #remove in case it exists
    return setup_logging(logs_filename)


