import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException


class DataIngestion:

    def __init__(self):

        self.raw_data_path = "artifacts/raw.csv"
        self.train_data_path = "artifacts/train.csv"
        self.test_data_path = "artifacts/test.csv"

    def initiate_data_ingestion(self):

        logger.info("========== Data Ingestion Started ==========")

        try:

            # Read Raw Dataset
            df = pd.read_csv("Data/raw/Crop_recommendation.csv")

            logger.info("Raw Dataset Loaded Successfully")

            # Create Artifacts Folder
            os.makedirs("artifacts", exist_ok=True)

            # Save Raw Dataset
            df.to_csv(self.raw_data_path, index=False)

            logger.info("Raw Dataset Saved")

            # Train-Test Split
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            train_set.to_csv(self.train_data_path, index=False)
            test_set.to_csv(self.test_data_path, index=False)

            logger.info("Train Dataset Saved")
            logger.info("Test Dataset Saved")

            logger.info("========== Data Ingestion Completed ==========")

            return (
                self.train_data_path,
                self.test_data_path
            )

        except Exception as e:

            raise CustomException(e, sys)
        
        
if __name__ == "__main__":

    obj = DataIngestion()

    train_path, test_path = obj.initiate_data_ingestion()

    print("Train Dataset:", train_path)
    print("Test Dataset :", test_path) 