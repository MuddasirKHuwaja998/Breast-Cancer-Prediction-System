# Breast Cancer Prediction Web App

## Overview

This project is a professional, production-ready web application that leverages **Machine Learning (Logistic Regression)** to predict whether a breast tumor is **benign** or **malignant** based on various cell sample features. The application is built with **Python (Flask)** for the backend, utilizes **scikit-learn** for modeling, and features a modern, dark-themed user interface styled with **HTML** and **CSS**.

---

## Features

- **User-Friendly Web Interface:** Enter cell sample features and get instant predictions.
- **Beautiful, Professional Dark Theme:** Modern and accessible design with green accents and easy-to-read layout.
- **Live ML Prediction:** Uses a Logistic Regression model trained on a real-world breast cancer dataset.
- **Educational:** Includes detailed explanations and tooltips to enhance understanding.
- **Branding:** Footer includes author and professional details.

---

## Dataset

- **Source:** [UCI Machine Learning Repository - Breast Cancer Wisconsin (Original)](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29)
- **Organization:** University of Wisconsin Hospitals, Madison, Dr. William H. Wolberg
- **Features Used:**
  - Clump Thickness
  - Uniformity of Cell Size
  - Uniformity of Cell Shape
  - Marginal Adhesion
  - Single Epithelial Cell Size
  - Bare Nuclei
  - Bland Chromatin
  - Normal Nucleoli
  - Mitoses
- **Target:** `Class`  
  - 2 = Benign (not cancerous)
  - 4 = Malignant (cancerous)

---

## How It Works

1. **User Inputs:** The user enters values for nine cell features, typically in the range 1–10.
2. **Prediction:** The trained logistic regression model processes these values and predicts whether the tumor is benign or malignant.
3. **Result:** The website displays a clear verdict along with all entered details.

---

## Professional Details

- **App Author:** Muddasir Khuwaja
- **Role:** AI/ML Engineer in the Medical Industry, Italy
- **GitHub:** [MuddasirKHuwaja998](https://github.com/MuddasirKHuwaja998)

---

## Getting Started

### 1. **Prerequisites**

- Python 3.8+
- pip

### 2. **Clone the Repository**

```sh
git clone https://github.com/MuddasirKHuwaja998/breast-cancer-prediction-app.git
cd breast-cancer-prediction-app
```

### 3. **Install Dependencies**

```sh
pip install flask scikit-learn pandas
```

### 4. **Project Structure**

```
C:\Users\Mudda\Desktop\Machine learning\Logistic Regression\
│   app.py
│   breast_cancer.csv
│
├───static
│       style.css
│
└───templates
        index.html
```

### 5. **Run the Application**

```sh
python app.py
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## Screenshots

![Web App Screenshot](screenshot.png)

---

## Acknowledgements

- **Data:** Sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29), courtesy of Dr. William H. Wolberg and the University of Wisconsin Hospitals, Madison.
- **Libraries:** Flask, scikit-learn, pandas.
- **Design & Implementation:** Muddasir Khuwaja

---

## Disclaimer

This tool is for educational and demonstration purposes only. **Always consult a qualified medical professional for real-world diagnosis and treatment decisions.**

---



---
