import logging


logger = logging.getLogger("jonin_logger")   # create a logger object
logger.setLevel(logging.DEBUG)    # set logger level

stream_handler = logging.StreamHandler()   # create stream handler object


formatter = logging.Formatter('%(asctime)s | [%(levelname)s] | %(message)s | [%(pathname)s:%(lineno)d]')   # ideal log format

# asctime : is a human read-able time attribute
# levelname : is a level for the log message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
# pathname : Full pathname of the source file where the logging call was issued.
# lineno : Source line number where the logging call was issue
# you can use different types of LogRecord attributes.

stream_handler.setFormatter(formatter)   # set formatter for stream handler


logger.addHandler(stream_handler)   # Add stream handler to logger


# Some logs to print on console ;-)
logger.info("A smile is the best way to get oneself out of a tight spot, even if it is a fake one - Sasuke.")
logger.warning("Those who cannot acknowledge themselves will eventually fail. - Itachi.")


print("Hi there !!!")