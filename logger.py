import logging
import os
import inspect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # src
PROJECT_ROOT = BASE_DIR                               # since src IS root
LOG_PATH = os.path.join(PROJECT_ROOT, "logs")


def get_logger():
    # Ensure logs directory exists
    os.makedirs(LOG_PATH, exist_ok=True)

    caller_frame = inspect.stack()[1]
    file_path = caller_frame.filename

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    module_name = os.path.basename(os.path.dirname(file_path))

    log_file_name = f"{module_name}_{file_name}.log"
    log_file_path = os.path.join(LOG_PATH, log_file_name)

    logger_name = f"{module_name}.{file_name}"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    
    # logger.propagate = False

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)


    return logger
