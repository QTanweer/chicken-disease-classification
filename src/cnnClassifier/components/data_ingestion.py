"""
Data Ingestion Component 
"""

import os
import urllib.request as request
from zipfile import ZipFile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    """
    Data Ingestion class
    """
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Download file from source url
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info("Downloaded file %s with the folowing headers: \n%s", filename, headers)
        else:
            logger.info(
                "File already exists at %s of size %s",
                  self.config.local_data_file,
                    get_size(self.config.local_data_file))

    def extract_zip_file(self):
        """
        extract the zip file
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(path=unzip_path)
            logger.info("Extracted file at %s", self.config.unzip_dir)
                