from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

model = joblib.load("burnout_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()


        df = pd.DataFrame([input_data])
        df = df[model.feature_names_in_]

        prediction = model.predict(df)[0]
        label = "Alto risco de burnout" if prediction == 1 else "Baixo risco de burnout"

        return jsonify({
            "prediction": int(prediction),
            "label": label
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)