from flask import Flask, render_template, request
import socket

app = Flask(__name__)


def classify(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height_cm = float(request.form["height"])
            if weight <= 0 or height_cm <= 0:
                raise ValueError
            bmi = weight / ((height_cm / 100) ** 2)
            result = {"bmi": round(bmi, 1), "category": classify(bmi)}
        except (ValueError, KeyError):
            error = "Please enter positive numbers for weight and height."
    return render_template("index.html", result=result, error=error,
                           hostname=socket.gethostname())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/health")
def health():
    return {"status": "ok", "host": socket.gethostname()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)