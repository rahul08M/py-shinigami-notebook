# python logging meta's

##### This Git repository contains a Python code snippets that implements logging to capture runtime information. The logging code helps to understand the application's behavior during runtime and can aid in debugging and troubleshooting. The repository includes all the necessary files and configurations to run the project locally or deploy it to a server.

### 1) [Simple python logging](https://github.com/rahul08M/py-shinigami-notebook/blob/main/logging/log_formats.py)
#### This is a simple example of how to use the Python logging module to log messages in your Python code.
The `log_formats.py` script contains a simple Python program that uses the logging module to log messages to the console and to a log file.

In this example, we set the log level to `DEBUG`, which means that all log messages with a level of `DEBUG` or higher will be logged. We also specify a format for the log messages, which includes the timestamp, logging level, and message text.

The `logging.debug()`, `logging.info()`, `logging.warning()`, `logging.error()`, and `logging.critical()` functions are used to log messages with different levels of severity. In this example, we log messages with info and warning levels to demonstrate how the logging module works. 

### 2) [Python logging on AWS Cloudwatch](https://github.com/rahul08M/py-shinigami-notebook/blob/main/logging/aws_cloudwatch_logger.py)
#### This is a simple example of how to use the Python logging module to send log messages to AWS CloudWatch.

## Prerequisites

Before running this code, you should have:

-   An AWS account with access to AWS CloudWatch.
-   AWS CLI installed and configured on your local machine.
-   Python 3.x installed on your local machine.

The `aws_cloudwatch_logger.py` script contains a simple Python program that uses the logging module and the AWS SDK for Python (Boto3) to send log messages to AWS CloudWatch.
