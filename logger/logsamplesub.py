'''
測試log到引用的class 也能輸出
'''
import logging

# create logger


class Tobj:
    def __init__(self,abc,logging):
        logger = logging.getLogger("logsamplesub") #("simpleExample")
        logger.info(abc)


