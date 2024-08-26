
from CNN_Classifier import logger, CustomException
try:

    logger.info("Running Scuccess")
    a = 1/0
    print(a)
    logger.info("Divide by error success.")
except Exception as e:
    logger.info("Caught Exception")
    raise CustomException(e)