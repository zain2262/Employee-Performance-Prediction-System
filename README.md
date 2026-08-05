# Employee Performance Prediction System

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random%20Forest-orange?logo=scikitlearn)
![HTML5](https://img.shields.io/badge/HTML-Frontend-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS-Styling-blue?logo=css3)
![License](https://img.shields.io/badge/License-MIT-green)

A **Machine Learning-based Employee Performance Prediction System** developed using **Python, Flask, HTML, CSS, and Scikit-learn**. The system predicts employee performance scores based on HR-related attributes and provides an interactive web interface with analytics and visualization.

---

#  Project Overview

Employee performance evaluation is an important task in Human Resource Management. This project uses a **Random Forest Classifier** to predict an employee's performance score based on various factors such as:

- Department
- Gender
- Age
- Job Title
- Years at Company
- Education Level
- Monthly Salary
- Projects Handled
- Training Hours
- Employee Satisfaction Score
- and more...

The prediction is displayed through a user-friendly Flask web application.

---

# Features

| Feature | Description |
|----------|-------------|
|  Machine Learning Prediction | Predict employee performance using Random Forest |
|  Flask Web Application | Interactive web interface |
|  Dashboard | HR analytics summary |
|  Charts | Performance Distribution, Heatmap & Feature Importance |
|  Responsive UI | HTML & CSS responsive design |
|  Performance Result | Shows prediction score with performance category |
|  About Page | Project information |
|  Contact Page | Contact interface |

---

#  Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Random Forest Classifier

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Web Development

- Flask
- HTML5
- CSS3

### Model Deployment

- Joblib

---

#  Project Structure

```text
Employee-Performance-Prediction-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── performance.csv
│
├── model/
│   └── performance_model.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── performance_distribution.png
│       ├── heatmap.png
│       └── feature_importance.png
│
└── templates/
    ├── index.html
    ├── result.html
    ├── dashboard.html
    ├── charts.html
    ├── about.html
    └── contact.html
```

---

#  Installation Guide

### 1️ Clone Repository

```bash
git clone https://github.com/Zain_ul_abedin/Employee-Performance-Prediction-System.git
```

### 2️ Go to Project Folder

```bash
cd Employee-Performance-Prediction-System
```

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️ Run Flask Application

```bash
python app.py
```

### 5️ Open Browser

```
http://127.0.0.1:5000
```

---

#  Machine Learning Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Label Encoding
      │
      ▼
Train-Test Split
      │
      ▼
Random Forest Classifier
      │
      ▼
Model Training
      │
      ▼
Save Model (.pkl)
      │
      ▼
Flask Integration
      │
      ▼
Performance Prediction
```

---

# 📷 Project Screenshots

##  Home Page

> Add screenshot here

```
screenshots/home.png
```

---

##  Dashboard

> Add screenshot here

```
screenshots/dashboard.png
```

---

##  Charts

> Add screenshot here

```
screenshots/charts.png
```

---

##  Prediction Result

> Add screenshot here

```
screenshots/result.png
```

---

# Dataset Features

- Employee_ID
- Department
- Gender
- Age
- Job_Title
- Years_At_Company
- Education_Level
- Monthly_Salary
- Work_Hours_Per_Week
- Projects_Handled
- Overtime_Hours
- Sick_Days
- Remote_Work_Frequency
- Team_Size
- Training_Hours
- Promotions
- Employee_Satisfaction_Score
- Resigned

###  Target Variable

```
Performance_Score
```

---

#  Machine Learning Model

| Algorithm | Random Forest Classifier |
|-----------|--------------------------|
| Problem Type | Multi-Class Classification |
| Target | Performance Score |
| Classes | 1–5 |

Performance Levels

| Score | Meaning |
|--------|---------|
| ⭐ 1 | Poor |
| ⭐⭐ 2 | Below Average |
| ⭐⭐⭐ 3 | Average |
| ⭐⭐⭐⭐ 4 | Good |
| ⭐⭐⭐⭐⭐ 5 | Excellent |

---

#  Future Improvements

-  User Authentication
-  MySQL Database Integration
-  Prediction History
-  PDF Report Generation
-  Email Notifications
-  Cloud Deployment
-  Live Dashboard Analytics

---

#  Author

**Zain ul abedin**

GitHub:
https://github.com/Zain2262

LinkedIn:
https://linkedin.com/in/Zain_ul_abedin

---

#  Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

##  License

This project is licensed under the MIT License.
