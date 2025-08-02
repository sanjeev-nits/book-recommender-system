import os
import sys
from six.moves import urllib
import zipfile

from books_recommender.exception.exception_handler import CustomException
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration

class DataIngestion:

    def __init__(self,app_config=AppConfiguration()):
        """Initialize Data Ingestion with application configuration."""
        try:
            logging.info("Initializing Data Ingestion")
            self.data_ingestion_config = app_config.get_data_ingestion_config()
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def download_data(self):
        """Download dataset from the specified URL."""
        try:
            dataset_url = self.data_ingestion_config.dataset_download_url
            zip_download_dir= self.data_ingestion_config.raw_data_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = os.path.basename(dataset_url)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading dataset from {dataset_url} to {zip_file_path}")
            urllib.request.urlretrieve(dataset_url, zip_file_path)
            logging.info("Dataset downloaded successfully")
            return zip_file_path
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def extract_zip_file(self,zip_file_path):
        """Extract the downloaded zip file."""
        try:
            ingested_dir=self.data_ingestion_config.ingested_data_dir
            os.makedirs(ingested_dir, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                logging.info(f"Extracting {zip_file_path} to {ingested_dir}")
                zip_ref.extractall(ingested_dir)
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def initiate_data_ingestion(self):
        """Main method to initiate data ingestion process."""
        try:
            logging.info("Starting data ingestion process")
            zip_file_path = self.download_data()
            self.extract_zip_file(zip_file_path=zip_file_path)
            logging.info("Data ingestion completed successfully")
        except Exception as e:
            raise CustomException(e, sys) from e


