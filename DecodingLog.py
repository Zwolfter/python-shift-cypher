import logging
def logEncoding(Message):
    logging.basicConfig(format='%(message)s',filename='Decodinglog.txt',level=logging.DEBUG)
    logging.info(Message)