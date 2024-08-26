import os
from box.exceptions import BoxValueError
import yaml
from CNN_Classifier import logger, CustomException
import json
import joblib 
from pathlib import Path
from typing import Any, List
import base64
from ensure import ensure_annotations
from box import ConfigBox


@ensure_annotations
def read_yaml(path :Path) -> ConfigBox :
    """
    Reads a Yaml and returns the content in box style.
    """
    try :
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML File {path} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError :
        logger.info("Caught Box Value Exception")
        raise CustomException(BoxValueError)
    except Exception as E:
        logger.exception(f"Caught Exception : {E}")
        raise CustomException(E)
    

@ensure_annotations
def create_directories(path_to_dir : List,verbose = True) -> None:
    """
    Create Empty Diectories specified in given path.
    """
    try : 
        for path in path_to_dir:
            os.makedirs(path,exist_ok=True)
            if verbose : 
                logger.info(f"Created Directory {path}")
    
    except Exception as e:
        logger.exception(f"Caught Exception : {e}")
        raise CustomException(e)

@ensure_annotations
def load_json(path :Path) ->ConfigBox:
    """
    Loading a jsonfile to BoxConfig.
    """
    try:
        with open(path) as json_file:
            content = json.load(json_file)
            logger.info(f"Loaded Json File {path}.")
            return ConfigBox(content)
    except BoxValueError :
        logger.info(f"Caught Box Exception : {BoxValueError}")
        raise CustomException(BoxValueError)

    except Exception as e:
        logger.exception(f"Caught Exception : {e}")
        raise CustomException(e)
    
@ensure_annotations
def save_json(path:Path,data:dict)->None:
    """
    Save Dictonary to json file in provided path.
    """
    try:
        with open(path,'w') as file:
            json.dump(data,file,indent=4)

            logger.info(f"Saved data to the Json File {path}.")
    except Exception as e:
        logger.exception(f"Caught Exception : {e}")
        raise CustomException(e)
    

@ensure_annotations
def save_bin(path:Path,data:Any)->None:
    """
    Saves Binary File to the object in local.
    """

    try:
        joblib.dump(data,path)
        logger.info(f"Saving Binary File in {path}")

    except Exception as e:
        logger.exception(f"Caught Exception: {e}")
        raise CustomException(e)
    
@ensure_annotations
def load_bin(path:Path) ->Any :
    """
    Load and return BInary File.
    """
    try:
        obj = joblib.load(path)
        logger.info(f"Binary File Loaded from : {path}")
        return obj
    
    except Exception as e:
        logger.exception(f"Caught Exception : {e}")
        raise CustomException(e) 

@ensure_annotations 
def get_size(path:Path)->str:
    """
    Get the size of file in KB of file.
    """
    try :
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"Size is {size_in_kb} kb."
    except Exception as e:
        logger.exception(f"Caught Exception : {e}")
        raise CustomException(e)
    

def decodeImage(imgstring, fileName):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, 'wb') as f:
            f.write(imgdata)
            f.close()
    except Exception as e:
        logger.exception(f"Caught Exception : {e}")
        raise CustomException(e)
    

def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
        
    except Exception as e:
        logger.exception(f"Caught Exception : {e}")
        raise CustomException(e)
    