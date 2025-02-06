import inspect
import logging


class Logger:
    def get_logger(self):
        LoggerName = inspect.stack()[1][3]
        logger = logging.getLogger(LoggerName)
        logger.setLevel(logging.INFO)

        # Create a file handler (you can customize file path and format)
        if not logger.handlers:  # Only add handler if it doesn't exist
            fileHandler = logging.FileHandler(
                '/Users/vikasdeswal/Documents/Projects/Amazon Automation/reports/testLogs.log')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

        return logger
