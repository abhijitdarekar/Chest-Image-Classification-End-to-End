import os 
import sys
import logging
from datetime import datetime


class Logger:
    def __init__(self,):

        self.__logging_format = '[%(asctime)s : %(levelname)s : %(module)s : %(message)s]'
        time = datetime.now()

        self.__log_dir = f"logs/{time.strftime('%Y_%m_%d')}"
        self.__log_file_name =time.strftime("%Y_%m_%d")#_%H_%M_%S")
        self.__logfile_path = os.path.join(self.__log_dir,f"log_{self.__log_file_name}.log")
        os.makedirs(self.__log_dir,exist_ok=True)
        logging.basicConfig(
            level = logging.INFO,
            format=self.__logging_format,
            handlers=[
                logging.FileHandler(self.__logfile_path),
                logging.StreamHandler(sys.stdout)      
            ]
        )
        self.get_logger = logging.getLogger("CNN_Classifer")


logger = Logger().get_logger

def ErrorMessageDetail(error, errorDetail:sys):
    _,_, error_tb = errorDetail.exc_info()
    fileName = error_tb.tb_frame.f_code.co_filename
    errorMessage = " Error Occured in Python Scrpt [{0}]| Line Number [{1}] | Message [{2}]".format(
        fileName, error_tb.tb_lineno, str(error)
    )
    return errorMessage

class CustomException(Exception):
    def __init__(self, errorMessage, errorDetail:sys):
        super().__init__(errorMessage)
        self.errorMessage = ErrorMessageDetail(errorMessage,errorDetail)

    def __str__(self) -> str:
        return self.errorMessage
    