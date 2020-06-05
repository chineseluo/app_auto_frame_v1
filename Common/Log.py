#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : api_request
@Time    : 2020/4/2 14:00
@Auth    : wrc
@Email   : wangrc@inhand.com.cn
@File    : Log.py
@IDE     : PyCharm
------------------------------------
"""
import logging
import logging.config
from os import path

from Common.publicMethod import PubMethod as pub_api

logger_config_path = path.dirname(__file__)
logging.config.dictConfig(pub_api.read_yaml(path.join(logger_config_path, 'logging.config.yml')))


class MyLog:
    def __init__(self):
        self.logger = logging.getLogger('mylogger')

    def __console(self, level, message):
        level = level.upper()
        if level == 'INFO':
            self.logger.info(message)
        elif level == 'DEBUG':
            self.logger.debug(message)
        elif level == 'WARNING':
            self.logger.warning(message)
        elif level == 'ERROR':
            self.logger.error(message)
        elif level == 'CRITICAL':
            self.logger.critical(message)

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def critical(self, message):
        self.__console('critical', message)


if __name__ == '__main__':
    s = MyLog()
    s.info('测试001')
