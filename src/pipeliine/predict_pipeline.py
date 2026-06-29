import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logger
from src.utils import load_object


class PredictPipeline:

    def __init__(self):

        self.model_path = "artifacts/model.pkl"
        self.encoder_path = "artifacts/label_encoder.pkl"

    def predict(self, features):

        try:

            logger.info("Prediction Started")

            # Load Model
            model = load_object(self.model_path)

            logger.info("Model Loaded Successfully")

            # Load Label Encoder
            label_encoder = load_object(self.encoder_path)

            logger.info("Label Encoder Loaded Successfully")

            # Prediction
            prediction = model.predict(features)

            logger.info("Prediction Completed")

            # Convert Number to Crop Name
            crop = label_encoder.inverse_transform(prediction)

            logger.info(f"Predicted Crop : {crop[0]}")

            return crop[0]

        except Exception as e:

            raise CustomException(e, sys)
        
class CustomData:

    def __init__(
        self,
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ):

        self.N = N
        self.P = P
        self.K = K
        self.temperature = temperature
        self.humidity = humidity
        self.ph = ph
        self.rainfall = rainfall

    def get_data_as_dataframe(self):

        try:

            data = {
                "N": [self.N],
                "P": [self.P],
                "K": [self.K],
                "temperature": [self.temperature],
                "humidity": [self.humidity],
                "ph": [self.ph],
                "rainfall": [self.rainfall]
            }

            return pd.DataFrame(data)

        except Exception as e:

            raise CustomException(e, sys)        