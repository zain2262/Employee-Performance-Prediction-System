# Employee Performance Prediction System

A **Machine Learning-based Employee Performance Prediction System** built with **Python, Flask, Pandas, NumPy, Scikit-learn, HTML, and CSS**.

The system predicts employee performance levels from **1 to 5** based on HR-related attributes and provides the prediction through an interactive Flask web application with dashboards and visual analytics.

---

## 📌 Project Overview

Employee performance evaluation is an important task in Human Resource Management.

This project uses a **Random Forest Classifier** with a preprocessing pipeline to predict an employee's performance score based on multiple factors, including:

* Department
* Gender
* Age
* Job Title
* Years at Company
* Education Level
* Monthly Salary
* Work Hours per Week
* Projects Handled
* Overtime Hours
* Sick Days
* Remote Work Frequency
* Team Size
* Training Hours
* Promotions
* Employee Satisfaction Score
* Resigned Status

The trained preprocessing pipeline and machine learning model are saved together in a `.pkl` file and integrated into the Flask application.

---

## ✨ Features

| Feature                        | Description                                               |
| ------------------------------ | --------------------------------------------------------- |
| 🤖 Machine Learning Prediction | Predicts employee performance using Random Forest         |
| 🔄 Preprocessing Pipeline      | Applies the same preprocessing used during model training |
| 🌐 Flask Web Application       | Interactive web-based prediction system                   |
| 📊 Dashboard                   | Provides HR-related analytics                             |
| 📈 Charts                      | Displays performance and feature-related visualizations   |
| 🎯 Performance Categories      | Converts scores into meaningful performance levels        |
| 📱 Responsive Interface        | User-friendly HTML/CSS interface                          |
| 📄 Result Page                 | Displays prediction score and performance category        |
| ℹ️ About Page                  | Provides project information                              |
| 📞 Contact Page                | Provides a contact interface                              |

---

## 🛠 Technologies Used

### Programming Language

* Python 3.11

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* Scikit-learn Pipeline
* ColumnTransformer
* OneHotEncoder

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Development

* Flask
* HTML5
* CSS3

### Model Persistence

* Joblib

---

## 📁 Project Structure

```text
Employee_performance_prediction/
│
├── app.py
├── dataset/
│
├── model/
│   └── performance_prediction_pipeline.pkl
│
├── static/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── dashboard.html
│   ├── charts.html
│   ├── about.html
│   └── contact.html
│
├── train_model.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

### Main Model File

The Flask application uses:

```text
model/performance_prediction_pipeline.pkl
```

This file contains the trained preprocessing pipeline and Random Forest model together.

---

# 🚀 Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/zain2262/Employee-Performance-Prediction-System.git
```

## 2. Navigate to the Project Folder

```bash
cd Employee-Performance-Prediction-System
```

## 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

The project uses **Scikit-learn 1.8.0** to maintain compatibility with the saved machine learning pipeline.

## 4. Run the Flask Application

```bash
python app.py
```

## 5. Open the Application

```text
http://127.0.0.1:5000
```

---

# 🧠 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Preparation
   │
   ▼
Feature Selection
   │
   ▼
Train-Test Split
   │
   ▼
Preprocessing Pipeline
   │
   ├── Categorical Feature Processing
   │
   └── Numerical Feature Processing
   │
   ▼
Random Forest Classifier
   │
   ▼
Model Evaluation
   │
   ▼
Save Complete Pipeline
   │
   ▼
Flask Integration
   │
   ▼
Employee Performance Prediction
```

---

# 📊 Model Evaluation

The model was evaluated on a test set containing **20,000 samples**.

| Metric       |  Result |
| ------------ | ------: |
| Test Samples |  20,000 |
| Accuracy     | 100.00% |
| Precision    |    1.00 |
| Recall       |    1.00 |
| F1-Score     |    1.00 |

The saved pipeline was also loaded independently and produced:

```text
Loaded Pipeline Accuracy: 1.0000
```

### ⚠️ Important Note

The reported 100% accuracy is based on this specific dataset and test split. It should not automatically be interpreted as 100% real-world predictive accuracy.

Dataset construction, feature relationships, class separability, and potential data leakage can affect the result.

---

# 🎯 Performance Levels

| Score | Performance Level         |
| ----: | ------------------------- |
|     1 | Poor Performance          |
|     2 | Below Average Performance |
|     3 | Average Performance       |
|     4 | Good Performance          |
|     5 | Excellent Performance     |

---

# 📋 Dataset Features

The dataset contains employee-related attributes including:

* Employee_ID
* Department
* Gender
* Age
* Job_Title
* Years_At_Company
* Education_Level
* Monthly_Salary
* Work_Hours_Per_Week
* Projects_Handled
* Overtime_Hours
* Sick_Days
* Remote_Work_Frequency
* Team_Size
* Training_Hours
* Promotions
* Employee_Satisfaction_Score
* Resigned

### Target Variable

```text
Performance_Score
```

The target contains five performance classes:

```text
1, 2, 3, 4, 5
```

---

# 🌐 Flask Application

The Flask application provides the following pages:

### Home

Employee information is entered through the prediction form.

### Prediction Result

Displays:

* Predicted performance score
* Performance category

### Dashboard

Provides an overview of employee performance-related analytics.

### Charts

Provides visualizations for understanding the dataset and model-related information.

### About

Contains information about the project and its purpose.

### Contact

Provides a contact interface.

---

# 📸 Project Screenshots

Screenshots can be added later inside a `screenshots/` folder.

## Home Page

```text
screenshots/home.png
```

## Dashboard

```text
screenshots/dashboard.png
```

## Charts

```text
screenshots/charts.png
```

## Prediction Result

```text
screenshots/result.png
```

---

# 🔮 Future Improvements

* User Authentication
* MySQL Database Integration
* Prediction History
* Employee Record Management
* PDF Report Generation
* Email Notifications
* Cloud Deployment
* Advanced Dashboard Analytics
* Model Monitoring
* Additional Model Comparison

---

# 👨‍💻 Author

**Zain ul Abedin**

### GitHub

https://github.com/zain2262

### LinkedIn

https://linkedin.com/in/Zain_ul_abedin

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the **MIT License**.

```
```
