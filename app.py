import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


def fetch_latest_model():
    model_path = os.path.abspath("artifacts/models/raw_model")
    temp = os.listdir(model_path)
    temp.sort()
    model_name = temp[-1]
    model_name_path = os.path.join(model_path,model_name)
    return model_name_path


model_name_path = fetch_latest_model()

model = pickle.load(open(model_name_path, 'rb'))

@app.route("/predict",methods=["GET","POST"])
def prediction():
    if request.method == "POST":
        data_dict = dict(request.form)
        area = float(data_dict["area"])
        pred = model.predict([[area]])[0][0]
        return render_template("test.html",prediction=pred)
    else:
        return render_template("test.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
    








