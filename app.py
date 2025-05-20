from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index_page():
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = weight / ((height / 100) ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "You are underweight!"
        elif 18.5 <= bmi <= 24.9:
            category = "You are of Normal weight"
        elif 25.0 <= bmi <= 29.9:
            category = "You are Overweight!"
        elif 30.0 <= bmi <= 34.9:
            category = "You have Obesity class I"
        elif 35.0 <= bmi <= 39.9:
            category = "You have Obesity class II"
        else:
            category = "You have Obesity class III"

    return render_template("BMI.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
