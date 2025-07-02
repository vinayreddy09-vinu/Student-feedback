
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    subject = request.form["subject"]
    rating = request.form["rating"]
    comments = request.form["comments"]
    with open("feedback.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, subject, rating, comments])
    return redirect("/summary")

@app.route("/summary")
def summary():
    feedbacks = []
    try:
        with open("feedback.csv", "r") as f:
            reader = csv.reader(f)
            feedbacks = list(reader)
    except FileNotFoundError:
        pass
    return render_template("summary.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
