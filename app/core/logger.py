import logging


class Logger:
    _logger = logging.getLogger('uvicorn.error')

    def __init__(self):
        raise Exception("Abstract class only")

    @staticmethod
    def debug(message: str):
        Logger._logger.debug(message)

    @staticmethod
    def info(message: str):
        Logger._logger.info(message)

    @staticmethod
    def warning(message: str):
        Logger._logger.warning(message)

    @staticmethod
    def error(message: str):
        Logger._logger.error(message)

    @staticmethod
    def critical(message: str):
        Logger._logger.critical(message)

    @staticmethod
    def set_level(level):
        Logger._logger.setLevel(level)
