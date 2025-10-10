import inspect
import logging
from pathlib import Path

class Logger:
    def get_logger(self):
        LoggerName = inspect.stack()[1][3]
        logger = logging.getLogger(LoggerName)
        logger.setLevel(logging.INFO)

        # Create a file handler (you can customize file path and format)
        if not logger.handlers:  # Only add handler if it doesn't exist
            current_file = Path(__file__)
            project_root = current_file.parent.parent
            log_file = project_root/"reports"/"testLogs.log"

            # Create directory if it doesn't exist
            log_file.parent.mkdir(parents=True, exist_ok=True)

            fileHandler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

        return logger
