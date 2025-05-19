import sys
import logging
from datetime import datetime
import os

# Setup logging
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Custom error handling function
def error_message_detail(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script: [{0}], line: [{1}], message: [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

# Custom Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_details=error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

# Example usage
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error caught.")
        raise CustomException(e, sys)
