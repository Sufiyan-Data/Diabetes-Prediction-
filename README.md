# 🧠 AI for Diabetes Prediction

This project uses machine learning algorithms to predict whether a person is likely to have diabetes based on various diagnostic features. It focuses on building predictive models, optimizing them through hyperparameter tuning, and evaluating their performance using both full and reduced feature sets.

---

## 📌 Project Objective

To develop an AI-powered model that can predict the likelihood of diabetes in a patient using input features such as glucose level, BMI, insulin, and more. The model is built with healthcare applications in mind, where early prediction can lead to faster diagnosis and intervention.

---

## 📊 Dataset

- **Source**: PIMA Indians Diabetes Dataset
- **Features:**
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- **Target:**
  - Outcome (`0` = No diabetes, `1` = Has diabetes)

---

## 🧪 ML Models Used

1. **Logistic Regression**
2. **Support Vector Machine (SVM)**
3. **Random Forest Classifier**

---

## 🧰 Key Components

- Train-test split of data
- Training models on different data sizes (1%, 10%, 100%)
- Hyperparameter tuning using GridSearchCV
- Model evaluation using:
  - Accuracy
  - F-beta score (β = 0.5)
  - Training and prediction time
- Feature importance analysis
- Reduced feature model comparison

---

## 🏁 Results

| Model Version              | Accuracy | F-beta Score |
|---------------------------|----------|--------------|
| Optimized - Full Features | 0.7727   | 0.6863       |
| Optimized - Top 3 Features| 0.7662   | 0.6727       |

➡️ Even with reduced features, the model performs almost as well — showing potential for lightweight prediction models in real-world applications.

---

## 📈 Feature Importance (Top 5)

1. Glucose
2. BMI
3. Age
4. Insulin
5. Pregnancies

---

## 💡 Use Cases

- **Clinical decision support**
- **Early diabetes risk screening**
- **Health apps with minimal inputs**
- **Low-resource prediction in rural/remote setups**

# 🩺 Diabetes Prediction App

A simple and interactive machine learning web app built using **Streamlit** to predict whether a patient is likely to have diabetes or not, based on medical input features.

## 📌 Project Overview

This app uses a trained **Logistic Regression** model (or any classification model you choose) on the famous **Pima Indians Diabetes Dataset** to classify patients as diabetic or non-diabetic. It allows real-time input through a user-friendly web interface.

---

## 🚀 Demo

![ai for db png](demo_screenshot.png)

🧪 **Sample Output:**  
> ✅ Patient is NOT Diabetic (Probability: 0.29)

🧪 **Sample Output:**  
> ⚠️ Patient is likely Diabetic (Probability: 0.82)

---

## 📂 Files in This Repo

| File               | Description                                           |
|--------------------|-------------------------------------------------------|
| `app.py`           | Streamlit app for user interface and prediction logic |
| `diabetes_model.pkl` | Trained ML model saved using joblib                 |
| `requirements.txt` | List of required Python libraries                     |
| `diabetes_predictor.ipynb` | Notebook used for model training and EDA       |

---

## 🛠 Tech Stack

- Python 🐍  
- Streamlit 🧼  
- scikit-learn 🤖  
- NumPy 🧮  
- pandas 📊  
- Matplotlib (for EDA) 📈

---

## ⚙️ How to Run the App Locally

### 🔧 Prerequisites:
Make sure you have Python installed. Then install the required libraries:
xt

### 📬 Contact

**Sufiyan B**  
📧 [syedsufiyan251@gmail.com](mailto:syedsufiyan251@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/syed-sufiyan-32995b232)  
📁 [Portfolio: MyGreatLearning Profile](https://www.mygreatlearning.com/eportfolio/b-sufiyan)


