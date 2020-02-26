import logging
import logging.config
import sys
import logsamplesub

# LEVELS = {'debug': logging.DEBUG,
#           'info': logging.INFO,
#           'warning': logging.WARNING,
#           'error': logging.ERROR,
#           'critical': logging.CRITICAL}

# if len(sys.argv) > 1:
#     level_name = sys.argv[1]
#     level = LEVELS.get(level_name, logging.NOTSET)
#     logging.basicConfig(level=level)

logging.config.fileConfig("logging.conf")
logging.info("this is root message")
# create logger
logger = logging.getLogger("logsample") #("simpleExample")
# logsamplesub.Tobj('a')
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical error message')
logsamplesub.Tobj('b',logging)