import logging


logger = logging.getLogger("jonin_logger")   # create a logger object
logger.setLevel(logging.DEBUG)    # set logger level

stream_handler = logging.StreamHandler()   # create stream handler object


formatter = logging.Formatter('%(asctime)s | [%(levelname)s] | %(message)s | [%(pathname)s:%(lineno)d]')   # ideal log format
stream_handler.setFormatter(formatter)   # set formatter for stream handler


logger.addHandler(stream_handler)   # Add stream handler to logger


# Some logs to print on console ;-)
logger.info("A smile is the best way to get oneself out of a tight spot, even if it is a fake one - Sasuke.")
logger.warning("Those who cannot acknowledge themselves will eventually fail. - Itachi.")


print("Hi there !!!")