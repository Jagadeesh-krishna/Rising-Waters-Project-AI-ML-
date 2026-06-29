from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("floods.save")
scaler = joblib.load("scaler.save")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict-page')
def predict_page():
    return render_template("predict.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        annual = float(request.form['annual'])
        janfeb = float(request.form['janfeb'])
        marmay = float(request.form['marmay'])
        junsep = float(request.form['junsep'])
        octdec = float(request.form['octdec'])

        data = np.array([[annual, janfeb, marmay, junsep, octdec]])
        data = scaler.transform(data)

        prediction = model.predict(data)[0]

        if prediction == 1:
            return render_template("flood.html")
        else:
            return render_template("noflood.html")

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)