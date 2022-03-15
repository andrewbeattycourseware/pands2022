# demonstrate logging
# attributes you can put in the basicConfig
#   level
#   filename
#   filemode
#   format
#       %(name)s - %(levelname)s - %(message)s -  %(asctime)s - %(lineno)d

import logging
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.ERROR)
logging.basicConfig(filename='./debugging.log',
    filemode='a', 
    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d')


name = 'joe'

logging.error("this is an error")
logging.critical("hiya")
logging.warning('dont know %s', name)
logging.info("still going")
logging.debug("and so is this")
