import sys

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from src.logger import logger
from src.exception import CustomException
from src.utils import save_object


class ModelTrainer:

    def __init__(self):

        self.model_path = "artifacts/model.pkl"

    def initiate_model_trainer(

        self,

        X_train,

        X_test,

        y_train,

        y_test

    ):

        try:

            logger.info("========== Model Training Started ==========")

            models = {

                "Logistic Regression": LogisticRegression(max_iter=1000),

                "KNN": KNeighborsClassifier(),

                "Decision Tree": DecisionTreeClassifier(random_state=42),

                "Random Forest": RandomForestClassifier(random_state=42)

            }

            results = []

            best_accuracy = 0

            best_model = None

            best_model_name = ""

            for name, model in models.items():

                logger.info(f"Training {name}")

                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)

                accuracy = accuracy_score(y_test, y_pred)

                precision = precision_score(
                    y_test,
                    y_pred,
                    average="weighted"
                )

                recall = recall_score(
                    y_test,
                    y_pred,
                    average="weighted"
                )

                f1 = f1_score(
                    y_test,
                    y_pred,
                    average="weighted"
                )

                results.append({

                    "Model": name,

                    "Accuracy": accuracy,

                    "Precision": precision,

                    "Recall": recall,

                    "F1 Score": f1

                })

                logger.info(f"{name} Accuracy : {accuracy}")

                if accuracy > best_accuracy:

                    best_accuracy = accuracy

                    best_model = model

                    best_model_name = name

            results_df = pd.DataFrame(results)

            results_df = results_df.sort_values(
                by="Accuracy",
                ascending=False
            ).reset_index(drop=True)

            print("\nModel Comparison\n")

            print(results_df)

            logger.info(f"Best Model : {best_model_name}")

            logger.info(f"Best Accuracy : {best_accuracy}")

            save_object(

                self.model_path,

                best_model

            )

            logger.info("Best Model Saved Successfully")

            logger.info("========== Model Training Completed ==========")

            return results_df

        except Exception as e:

            raise CustomException(e, sys)

if __name__ == "__main__":

    from src.components.data_transformation import DataTransformation

    obj = DataTransformation()

    X_train, X_test, y_train, y_test = obj.initiate_data_transformation()

    trainer = ModelTrainer()

    trainer.initiate_model_trainer(

        X_train,

        X_test,

        y_train,

        y_test

    )        