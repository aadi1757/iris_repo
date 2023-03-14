from flask import Flask, render_template, request
from app.utils import Prediction

app = Flask(__name__)

@app.route("/")
def strat():
    return render_template(r"iris_html.html")

@app.route('/predict', methods = ["POSt", "GET"])
def predict_specie():
    data = request.form
    pred_obj = Prediction()
    predicted_specie = pred_obj.predict_specie(data)
    print(predicted_specie)

    return str(predicted_specie)


if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=8000,debug=False)


