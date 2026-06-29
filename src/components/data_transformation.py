import sys

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from src.logger import logger
from src.exception import CustomException
from src.utils import save_object


class DataTransformation:

    def __init__(self):

        self.train_path = "artifacts/train.csv"
        self.test_path = "artifacts/test.csv"

    def initiate_data_transformation(self):

        try:

            logger.info("========== Data Transformation Started ==========")

            train_df = pd.read_csv(self.train_path)
            test_df = pd.read_csv(self.test_path)

            logger.info("Train and Test Dataset Loaded Successfully")

            # Label Encoding
            label_encoder = LabelEncoder()

            train_df["label"] = label_encoder.fit_transform(train_df["label"])
            test_df["label"] = label_encoder.transform(test_df["label"])

            logger.info("Label Encoding Completed")

            # Save Label Encoder
            save_object(
                "artifacts/label_encoder.pkl",
                label_encoder
            )

            logger.info("Label Encoder Saved Successfully")

            # Features and Target
            X_train = train_df.drop("label", axis=1)
            y_train = train_df["label"]

            X_test = test_df.drop("label", axis=1)
            y_test = test_df["label"]

            logger.info("Features and Target Separated Successfully")

            logger.info("========== Data Transformation Completed ==========")

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:

            raise CustomException(e, sys)

if __name__ == "__main__":

    obj = DataTransformation()

    X_train, X_test, y_train, y_test = obj.initiate_data_transformation()

    print("X Train Shape :", X_train.shape)
    print("X Test Shape  :", X_test.shape)
    print("Y Train Shape :", y_train.shape)
    print("Y Test Shape  :", y_test.shape)        