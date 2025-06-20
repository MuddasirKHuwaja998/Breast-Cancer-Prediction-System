from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# --- Load and prepare the model at startup ---
df = pd.read_csv("C:\\Users\\Mudda\\Desktop\\Machine learning\\Logistic Regression\\breast_cancer.csv")

X = df.drop('Class', axis=1)
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

FEATURES = list(X.columns)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    cancer_type = None
    user_input = {}
    if request.method == "POST":
        try:
            input_values = []
            for feature in FEATURES:
                val = float(request.form.get(feature))
                user_input[feature] = val
                input_values.append(val)
            input_df = pd.DataFrame([input_values], columns=FEATURES)
            pred = model.predict(input_df)[0]
            prediction = int(pred)
            if prediction == 2:
                cancer_type = "Benign (Not Cancerous)"
            else:
                cancer_type = "Malignant (Cancerous)"
        except Exception as e:
            prediction = "Error"
            cancer_type = str(e)
    return render_template("index.html", features=FEATURES, prediction=prediction, cancer_type=cancer_type, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)