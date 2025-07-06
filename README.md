#  GlucoAI – Smart Diabetes Risk Predictor

"GlucoAI" is a smart and user-friendly web application that predicts the risk of diabetes using Machine Learning models (Random Forest, Logistic Regression, XGBoost) integrated with a Django-based frontend.

> "We ML models are working on it to make you safe "

---

## Features

-  User Signup/Login (Role-based: Patient or Doctor)
-  Diabetes prediction using ML models
-  ML loading screen with animated robot
-  Educational page to learn about diabetes
-  Accuracy-focused hybrid model using `XGBoost` and `Logistic Regression`
-  Role-based experience (doctors can view more, patients just predict)
-  Clean, animated UI using custom images and static files

---

##  Tech Stack

| Layer       | Tools Used                            |
|-------------|----------------------------------------|
| Frontend    | HTML, CSS, Django Templates            |
| Backend     | Django, Python                         |
| Machine Learning | XGBoost, Logistic Regression, Random Forest |
| Auth        | Django Auth, CustomUser model          |
| Database    | SQLite (local) / PostgreSQL (optional) |

---

##  Screenshots

| Login Page | ML Prediction Loader | Result |
|------------|----------------------|--------|
---

## How to Run Locally

### 1. Clone this repo:

git clone https://github.com/skyakash19/glucoai.git
cd glucoai
2. Install dependencies:

pip install -r requirements.txt
If you don’t have a requirements.txt, run:
pip freeze > requirements.txt
3. Run migrations:
python manage.py makemigrations
python manage.py migrate
4. Train ML models
python predictor/train_model.py
5. Start the server:
python manage.py runserver

User Roles
Role	Access
Patient	Predict diabetes risk
Doctor	(Coming Soon) View predictions of other users

Status
Currently in development
Fully working locally with ML models
Deployment to cloud: Coming Soon

Contribution :
Open to collaboration for:
Doctor dashboard
Graphical risk charts


Contact : 
Akash R A
NIE Mysore, India
+91 866 049 7408
akashrelekar1904@gmail.com
