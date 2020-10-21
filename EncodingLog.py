import logging
def logEncoding(Message):
    logging.basicConfig(format='%(message)s',filename='Encodinglog.txt',level=logging.DEBUG)
    logging.info(Message)