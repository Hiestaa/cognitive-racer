# -*- coding: utf8 -*-

# from __future__ import unicode_literals

### Initialize the logging system
import logging
import os
from conf import conf

from logging.handlers import RotatingFileHandler


def init(verbose=0, quiet=False, filename='activity.log'):
    """
    Initialize the logger
    * verbose (int) specify the verbosity level of the standart output
      0 (default) ~ ERROR, 1 ~ WARN & WARNING, 2 ~ INFO, 3 ~ DEBUG
    * quiet (boolean) allow to remove all message whatever is the verbosity lvl
    """
    if not os.path.exists('log'):
        os.mkdir('log')

    with open("log/" + filename, 'w'):
        pass

    logger = logging.getLogger()
    logger.propagate = False
    logger.setLevel(min([
        conf['logging']['log_file_level'], 
        conf['logging']['log_console_level'], 
        verbose]))

    formatter = logging.Formatter(
        '%(asctime)s :: %(levelname)s :: ' +
        '%(filename)s:%(funcName)s[%(lineno)d] :: %(message)s')
    file_handler = RotatingFileHandler("log/" + filename, 'w', 10000000, 10)
    file_handler.setLevel(conf['logging']['log_file_level'])
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    formatter = logging.Formatter(
        '%(asctime)s :: %(levelname)s :: ' +
        '%(filename)s:%(funcName)s[%(lineno)d] :: %(message)s')
    file_handler = RotatingFileHandler("log/errors.log", 'w', 10000000, 10)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    formatter = logging.Formatter(
        '%(levelname)s :: %(filename)s :: %(message)s')
    stream_handler = logging.StreamHandler()
    if verbose is -1:
        stream_handler.setLevel(conf['logging']['log_file_level'])
    elif verbose is 0:
        stream_handler.setLevel(logging.ERROR)
    elif verbose is 1:
        stream_handler.setLevel(logging.WARNING)
    elif verbose is 2:
        stream_handler.setLevel(logging.INFO)
    elif verbose is 3:
        stream_handler.setLevel(logging.DEBUG)
    elif verbose is 4:
        stream_handler.setLevel(0)
    else:
        stream_handler.setLevel(conf['logging']['log_console_level'])
    stream_handler.setFormatter(formatter)
    if not quiet:
        logger.addHandler(stream_handler)

    logging.info("=" * 80)
    logging.info('Logging system started: verbose=%d, quiet=%s' %
                 (verbose, str(quiet)))
