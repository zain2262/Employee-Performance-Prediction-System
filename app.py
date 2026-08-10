from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained pipeline
pipeline = joblib.load("model/performance_prediction_pipeline.pkl")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Charts Page
@app.route("/charts")
def charts():
    return render_template("charts.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Prediction
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
    Employee_Satisfaction_Score = float(
        request.form["Employee_Satisfaction_Score"]
    )
    Resigned = int(request.form["Resigned"])

    # Create DataFrame
    features = pd.DataFrame([{
        "Department": Department,
        "Gender": Gender,
        "Age": Age,
        "Job_Title": Job_Title,
        "Years_At_Company": Years_At_Company,
        "Education_Level": Education_Level,
        "Monthly_Salary": Monthly_Salary,
        "Work_Hours_Per_Week": Work_Hours_Per_Week,
        "Projects_Handled": Projects_Handled,
        "Overtime_Hours": Overtime_Hours,
        "Sick_Days": Sick_Days,
        "Remote_Work_Frequency": Remote_Work_Frequency,
        "Team_Size": Team_Size,
        "Training_Hours": Training_Hours,
        "Promotions": Promotions,
        "Employee_Satisfaction_Score": Employee_Satisfaction_Score,
        "Resigned": Resigned
    }])

    # Prediction
    prediction = int(pipeline.predict(features)[0])

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

    # Send result to result.html
    return render_template(
        "result.html",
        prediction=prediction,
        message=message
    )


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)

