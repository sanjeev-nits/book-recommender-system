import os
import sys

from books_recommender.exception.exception_handler import CustomException
from books_recommender.logger.log import logging
from books_recommender.utils.util import read_yaml
from books_recommender.entity.config_entity import DataingestionConfig,DataValidationConfig
from books_recommender.constant import *

class AppConfiguration:
    def __init__(self, config_file_path: str=CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml(file_path=config_file_path)
        except Exception as e:
            raise CustomException(e, sys)
        
    def get_data_ingestion_config(self) -> DataingestionConfig:
        try:
            data_ingestion_config=self.configs_info['data_ingestion_config']
            artifact_dir = self.configs_info['artifacts_config']['artifact_dir']
            dataset_dir= data_ingestion_config['dataset_dir']

            ingested_data_dir = os.path.join(artifact_dir, dataset_dir, data_ingestion_config['ingested_data_dir'])
            raw_data_dir = os.path.join(artifact_dir, dataset_dir, data_ingestion_config['raw_data_dir'])

            response = DataingestionConfig(
                dataset_download_url=data_ingestion_config['dataset_download_url'],
                raw_data_dir=raw_data_dir,
                ingested_data_dir=ingested_data_dir
            )
            logging.info(f"Data Ingestion Config: {response}")
            return response

            
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            data_validation_config = self.configs_info['data_validation_config']
            data_ingestion_config = self.configs_info['data_ingestion_config']
            dataset_dir = data_ingestion_config['dataset_dir']
            artifacts_dir = self.configs_info['artifacts_config']['artifact_dir']
            book_csv_file = data_validation_config['book_csv_file']
            ratings_csv_file = data_validation_config['ratings_csv_file']

            book_csv_file_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_data_dir'], book_csv_file)
            ratings_csv_file_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_data_dir'], ratings_csv_file)
            clean_data_path = os.path.join(artifacts_dir, dataset_dir, data_validation_config['clean_data_dir'])
            serialized_objects_dir = os.path.join(artifacts_dir, data_validation_config['serialized_objects_dir'])

            response = DataValidationConfig(
                clean_data_dir=clean_data_path,
                book_csv_file=book_csv_file_dir, 
                ratings_csv_file=ratings_csv_file_dir,
                serialized_objects_dir=serialized_objects_dir
)

            logging.info(f"Data Validation Config: {response}")
            return response

        except Exception as e:
            raise CustomException(e, sys) from e