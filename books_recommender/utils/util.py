import yaml
import sys
from books_recommender.exception.exception_handler import CustomException



def read_yaml(file_path:str)->dict:

    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise CustomException(e,sys)