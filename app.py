from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load Trained Model
model = joblib.load("model/performance_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/charts")
def charts():
    return render_template("charts.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["POST"])
def predict():

    # Get data from form
    Department = int(request.form["Department"])
    Gender = int(request.form["Gender"])
    Age = int(request.form["Age"])
    Job_Title = int(request.form["Job_Title"])
    Years_At_Company = int(request.form["Years_At_Company"])
    Education_Level = int(request.form["Education_Level"])
    Monthly_Salary = float(request.form["Monthly_Salary"])
    Work_Hours_Per_Week = int(request.form["Work_Hours_Per_Week"])
    Projects_Handled = int(request.form["Projects_Handled"])
    Overtime_Hours = int(request.form["Overtime_Hours"])
    Sick_Days = int(request.form["Sick_Days"])
    Remote_Work_Frequency = int(request.form["Remote_Work_Frequency"])
    Team_Size = int(request.form["Team_Size"])
    Training_Hours = int(request.form["Training_Hours"])
    Promotions = int(request.form["Promotions"])
    Employee_Satisfaction_Score = float(request.form["Employee_Satisfaction_Score"])
    Resigned = int(request.form["Resigned"])

    # Create feature array
    features = np.array([[
        Department,
        Gender,
        Age,
        Job_Title,
        Years_At_Company,
        Education_Level,
        Monthly_Salary,
        Work_Hours_Per_Week,
        Projects_Handled,
        Overtime_Hours,
        Sick_Days,
        Remote_Work_Frequency,
        Team_Size,
        Training_Hours,
        Promotions,
        Employee_Satisfaction_Score,
        Resigned
    ]])

    # Prediction
    prediction = int(model.predict(features)[0])

    # Performance Message
    if prediction == 1:
        message = "Poor Performance"

    elif prediction == 2:
        message = "Below Average Performance"

    elif prediction == 3:
        message = "Average Performance"

    elif prediction == 4:
        message = "Good Performance"

    else:
        message = "Excellent Performance"

    return render_template(
        "result.html",
        prediction=prediction,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)