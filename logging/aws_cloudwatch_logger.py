import watchtower
# https://pypi.org/project/watchtower/

import logging


LOG_GROUP_NAME = "meta"   # constant variable with group name
# The name of the log group from which logs data was exported.

LOG_STREAM_NAME = "meta_strem"   # constant variable with stream name
# The name of the log stream.

logging.basicConfig(level=logging.INFO)   # basic config for logging
logger = logging.getLogger(__name__)   # get logger for current file

aws_handler = watchtower.CloudWatchLogHandler(log_group_name=LOG_GROUP_NAME, log_stream_name=LOG_STREAM_NAME)   # handler for aws logging

logger.setLevel(logging.INFO)    # set the log level
logger.addHandler(aws_handler)    # add the handler

logger.info("Naruto and his team raced through the forest, dodging shuriken and kunai while searching for their next mission target.")

print("Hi there AWS !!! Shinobi")
