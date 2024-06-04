import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")
"""
Logging helps developers understand what went wrong when an error occurs. By examining the log messages
 they can trace the sequence of events that led to the error.
 Logs provide a record of system activity, which is essential for audits and security reviews.

logging: The built-in logging module in Python, which allows for the generation and customization of log messages.

logging_str: Defines the format string for log messages. The placeholders will be replaced by:
%(asctime)s: The time when the log message was created.
%(levelname)s: The severity level of the log message (e.g., INFO, WARNING, ERROR).
%(module)s: The name of the module where the log message was generated.
%(message)s: The actual log message.

log_dir: The name of the directory where log files will be stored.
log_filepath: The full file path for the log file, created by joining the directory name with the log file name.
os.makedirs(log_dir, exist_ok=True): Creates the directory logs if it does not already exist. The exist_ok=True
parameter prevents an error if the directory already exists.

logging.basicConfig: Configures the logging module.
level=logging.INFO: Sets the logging level to INFO, which means that all messages with a severity level of INFO and above will be logged.
When you set level=logging.INFO, it means that the logger will process and output log messages that are of level
INFO, WARNING, ERROR, and CRITICAL, but it will ignore DEBUG messages.
format=logging_str: Sets the format of the log messages to the previously defined format string.
handlers: Specifies where the log messages should be sent:
logging.FileHandler(log_filepath): Writes log messages to the specified file.
logging.StreamHandler(sys.stdout): Outputs log messages to the console (standard output).

"""