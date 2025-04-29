# Credit Card Fraud Detection System 🚀

---

## Live Demo

You can view the deployed project here: [Live Link](https://credit-card-fraud-detection-system-frgp.onrender.com)


## 🛡️ Problem Statement

Credit card fraud is a major threat in today's digital economy, costing billions annually.  
With the increasing volume of online transactions, detecting fraudulent activities becomes vital to protect both businesses and consumers.  
The objective of this project is to build a robust machine learning system capable of accurately identifying fraudulent credit card transactions.

---

## 📚 Abstract

Credit card fraud involves unauthorized transactions performed either by physically stealing a card or accessing sensitive card information digitally.  
This project focuses on developing a machine learning-based fraud detection model using real transaction data, where advanced algorithms are trained to recognize patterns indicative of fraudulent behavior.  
Special emphasis is placed on handling class imbalance, which is common in fraud detection datasets.

> **Keywords:** Credit Card Fraud Detection, Machine Learning, Logistic Regression, Decision Tree, Random Forest, Fraudulent Transactions , Handling Imbalanced Dataset

---

## 🗂️ Dataset Information

- **Source:** [Kaggle - Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download&select=creditcard.csv)
- **Rows:** 284,808 transactions
- **Columns:** 31 features:
  - **V1 to V28**: PCA-transformed anonymized features
  - **Time**: Seconds elapsed between transactions (dropped during modeling)
  - **Amount**: Transaction amount (scaled before modeling)
  - **Class**: Target variable (1 = Fraud, 0 = Genuine)

The dataset is highly **imbalanced** with a very small percentage of fraudulent transactions (~0.17%).

---

## 🏗️ Project Pipeline

1. **Data Collection**
   - Retrieved from Kaggle open-source platform.
   
2. **Data Preprocessing**
   - Dropped the `Time` feature.
   - Scaled the `Amount` feature using StandardScaler.
   - Ensured correct formatting for machine learning models.
   - Removed Duplicates
   
3. **Handling Class Imbalance**
   - **Undersampling** was initially applied by reducing the number of non-fraud cases to match the number of fraud cases.
   - **Oversampling** was later performed using techniques like SMOTE to synthetically generate fraudulent cases.
   - **Oversampling** delivered **higher performance** and was chosen for final model training.

4. **Exploratory Data Analysis (EDA)**
   - Checked class distribution.
   - Visualized transaction patterns and feature correlations.

5. **Model Building**
   - Trained multiple machine learning models including Logistic Regression, Decision Tree, and Random Forest.

6. **Model Evaluation**
   - Evaluated models using Accuracy, Precision, Recall, and F1-Score.
   - Focused primarily on Recall to reduce false negatives (missing actual frauds).

7. **Deployment**
   - Developed a simple **Flask web application** with two pages:
     - Project Overview
     - Fraud Prediction
     - The Flask application is deployed on Render.

---

## ⚙️ Algorithms Used

| Algorithm                 | Purpose                                         |
|----------------------------|--------------------------------------------------|
| Logistic Regression        | Baseline model for binary classification        |
| Decision Tree Classifier   | Tree-structured model capturing complex patterns |
| Random Forest Classifier   | Ensemble model to improve robustness and performance |

---

## 📊 Performance Highlights

- Dataset was highly **imbalanced**, so traditional accuracy was not a reliable metric.
- **Recall** was prioritized to minimize undetected fraud cases.
- **Random Forest Classifier** outperformed other models with a strong Recall and Precision after oversampling.
- Models after **oversampling** showed significantly better detection of fraud transactions compared to undersampling.
<p align="center">
  <img src="https://github.com/user-attachments/assets/3a498fa8-cd0c-4f67-9c55-6f78f2cc18a4" alt="ConverseLearn Banner" width="600"/>
</p>


---

## 🌟 Project Features

- **User-friendly Flask Web App**:
  - Light blue-themed interface for better UX.
  - "Project Overview" page describing methodology and workflow.
  - "Prediction" page allowing users to input transaction data and get real-time predictions.

<!-- Image 3 -->
<div align="center">
  <img src="https://github.com/user-attachments/assets/9404f04e-59f5-422d-a4d5-f214bfee03c8" alt="Image" width="700" height="400"/>
</div>

<br><br>

<!-- Image 4 -->
<div align="center">
  <img src="https://github.com/user-attachments/assets/99a6df08-67c9-403d-bf49-3f7374d2b5c6" alt="Image" width="700" height="400"/>
</div>


- **Input Handling**:
  - Accepts 30 features (Time, V1–V28, Amount) space-separated.
  - Automatically scales the Amount field.
  - Ignores Time internally during prediction.
- **Deployment**: The Flask application is deployed on Render.

---

## 🔮 Future Improvements

- Implement ensemble techniques like **XGBoost** and **LightGBM**.
- Test models on different datasets with various features and distributions.
- Build a real-time fraud detection pipeline with streaming data.
- Integrate geo-location and device fingerprinting features for multi-factor fraud detection.

---

## 🏆 Conclusion

The project successfully demonstrates the use of machine learning to detect fraudulent transactions with high accuracy and recall.  
By addressing class imbalance and choosing appropriate models, a robust fraud detection system was created.  
The system was further deployed as a simple Flask application, making it easy to integrate with real-world systems and enhancing customer trust and transaction security.

---

## 🔗 Useful Links

- 📁 **Dataset:** [Credit Card Fraud Dataset (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- 🛠 **Model File:** `credit_card_fraud_detection_model.pkl`
- 🌐 **Web Pages:** [Web Page](https://credit-card-fraud-detection-system-frgp.onrender.com)

---
