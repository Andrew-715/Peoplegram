import logging

_log_format = f'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%lineno)d) - %(message)s'


def get_file_handler():
    file_handler = logging.FileHandler('x.log')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    return logger
