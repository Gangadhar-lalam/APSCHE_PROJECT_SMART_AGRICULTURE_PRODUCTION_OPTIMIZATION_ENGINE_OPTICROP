import os
import sys
import pickle

from src.logger import logger
from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save Python object as Pickle file.
    """

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:

            pickle.dump(obj, file_obj)

        logger.info(f"Object saved successfully at {file_path}")

    except Exception as e:

        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load Pickle object.
    """

    try:

        with open(file_path, "rb") as file_obj:

            obj = pickle.load(file_obj)

        logger.info(f"Object loaded successfully from {file_path}")

        return obj

    except Exception as e:

        raise CustomException(e, sys)