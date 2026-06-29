from flask import Flask, request, render_template

from src.pipeliine.predict_pipeline import PredictPipeline, CustomData

app = Flask(__name__)


@app.route("/")
def home():
    print("Home route accessed")
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = CustomData(

            N=float(request.form["N"]),

            P=float(request.form["P"]),

            K=float(request.form["K"]),

            temperature=float(request.form["temperature"]),

            humidity=float(request.form["humidity"]),

            ph=float(request.form["ph"]),

            rainfall=float(request.form["rainfall"])

        )

        final_data = data.get_data_as_dataframe()

        predict_pipeline = PredictPipeline()

        prediction = predict_pipeline.predict(final_data)

        return render_template(
            "result.html",
            prediction=prediction
        )

    except Exception as e:

        return render_template(
            "result.html",
            prediction=f"Error: {str(e)}"
        )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=4002,
        debug=True
    )