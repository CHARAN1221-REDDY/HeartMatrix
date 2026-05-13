from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    cholesterol = int(request.form["cholesterol"])
    bp = int(request.form["bp"])
    hr = int(request.form["hr"])

    prediction = model.predict([[age, cholesterol, bp, hr]])

    if prediction[0] == 1:

        result = "⚠ High Risk of Heart Disease"

        diet = [
            "Oats and whole grains",
            "Green leafy vegetables",
            "Fresh fruits (apple, berries)",
            "Low-fat dairy products"
        ]

        avoid = [
            "Fried foods",
            "Processed meat",
            "High cholesterol foods",
            "Sugary drinks"
        ]

        exercise = "30 minutes walking or light cardio daily."

        medicine = "Consult a cardiologist and monitor blood pressure regularly."

    else:

        result = "✅ Low Risk of Heart Disease"

        diet = [
            "Balanced healthy diet",
            "Vegetables and fruits",
            "Whole grains",
            "Lean protein foods"
        ]

        avoid = [
            "Excess junk food",
            "Too much sugar",
            "Overeating"
        ]

        exercise = "Regular exercise for 20–30 minutes daily."

        medicine = "Maintain healthy lifestyle and regular health checkups."

    return render_template(
        "index.html",
        prediction_text=result,
        diet=diet,
        avoid=avoid,
        exercise=exercise,
        medicine=medicine
    )

if __name__ == "__main__":
    app.run(debug=True)