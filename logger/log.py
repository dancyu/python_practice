'''
return logger
'''

import logging
import logging.config


def getLogger(modulename):
    logging.config.fileConfig("logging.conf")
    return logging.getLogger(modulename)

