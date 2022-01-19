from flask import Flask
from flask import Flask, render_template, request
import sklearn
import pickle

model = pickle.load(open("static/model/model.sav", 'rb'))
sc = pickle.load(open('static/model/scaler.pkl', 'rb'))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/heart-disease-predictor", methods=['POST', 'GET'])
def heartDiseasePredictor():
    if request.method == 'POST':
        result = request.form.to_dict()
        age = int(result['age'])
        gender = int(result['gender'])
        chest_pain_type = int(result['chest-pain-type'])
        fasting_blood_sugar = int(result['fasting-blood-sugar'])
        induced_agina = int(result['induced-agina'])
        resting_blood_pressure = int(result['resting-blood-pressure'])
        peak_exercise_st = int(result['peak-exercise-st'])
        st_depression_value = float(result['st-depressed-value'])
        heart_rate_value = int(result['heart-rate-value'])
        serum_cholestrol_value = int(result['serum-cholestrol-value'])
        resting_ecg = int(result['resting-ecg'])
        element = sc.transform([[age, gender, chest_pain_type, resting_blood_pressure, serum_cholestrol_value,
                               fasting_blood_sugar, resting_ecg, heart_rate_value, induced_agina, st_depression_value, peak_exercise_st]])
        prediction_prob = model.predict_proba((element)).max()
        prediction = model.predict((element))
        print(prediction_prob)
        print(prediction)
        return render_template("result.html", results=result, prediction=prediction, prediction_prob=prediction_prob)
    return render_template("heart_disease.html")


if __name__ == "__main__":
    app.run()
