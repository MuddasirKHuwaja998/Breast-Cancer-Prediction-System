#lets do logistic regression 
# # Goal:Use the measurements of cells to automatically predict if a breast tumor is cancerous (malignant) or not (benign).
#Tool: Logistic Regression (a classification algorithm).
#Why: To help doctors quickly and accurately identify cancer using cell sample data.
#In the common "breast cancer" datasets, "Class" usually refers to:
#2 = Benign (not cancer)
#4 = Malignant (cancer)

# Import  the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix


#1let's load the dataset
load_data = pd.read_csv(r"C:\Users\Mudda\Desktop\Machine learning\Logistic Regression\breast_cancer.csv")
#lets exploare the data and print 1st 5 rows
print(load_data.head())


# let's inform the model out input and target feature
X = load_data.drop('Class', axis=1)
y = load_data['Class']
#Lets's split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



#lets initialiate our Model
model = LogisticRegression(max_iter=1000)# increasing max iteration to ensure convergence
# let's train the model
model.fit(X_train, y_train)
#lets make it predictions
predictions = model.predict(X_test)
#printing the preditions
print("predictions: ", predictions)


#Let's take input from user 
patient_name = input("Enter you name : ")
patient_age = input("Enter you age: ")
Clump_Thickness= float(input("Enter clump thickness (1-10): "))
Uniformity_of_Cell_Size= float(input("Enter uniformity of cell size (1-10): "))
Uniformity_of_Cell_Shape= float(input("Enter uniformity of cell shape (1-10): "))
Marginal_Adhesion= float(input("Enter marginal adhesion (1-10): "))
Single_Epithelial_Cell_Size= float(input("Enter single epithelial cell size (1-10): "))
Bare_Nuclei= float(input("Enter bare nuclei (1-10): "))
Bland_Chromatin= float(input("Enter bland chromatin (1-10): "))
Normal_Nucleoli= float(input("Enter normal nucleoli (1-10): "))
Mitoses= float(input("Enter mitoses (1-10): "))
user_input_df = pd.DataFrame([[Clump_Thickness, Uniformity_of_Cell_Size, Uniformity_of_Cell_Shape,
                               Marginal_Adhesion, Single_Epithelial_Cell_Size, Bare_Nuclei,
                               Bland_Chromatin, Normal_Nucleoli, Mitoses]],
                              columns=X.columns)
if model.predict(user_input_df)[0] == 2:
    print("You are predicted to have a Benign tumor (not cancerous).")
else:
    print("You are predicted to have a Malignant tumor (cancerous).")
print(f"Hello Mr. {patient_name}, aged {patient_age}, based on your details here is your cancer status prediction: ")
if model.predict([[Clump_Thickness, Uniformity_of_Cell_Size, Uniformity_of_Cell_Shape, Marginal_Adhesion, Single_Epithelial_Cell_Size, Bare_Nuclei, Bland_Chromatin, Normal_Nucleoli, Mitoses]])[0] == 2:
    print("You are predicted to have a Benign tumor (not cancerous).")
else:
    print("You are predicted to have a Malignant tumor (cancerous).")

#Lets evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: ", accuracy)
print("model classification report :\n", classification_report(y_test, predictions))
# lets print confusion matrix
print("confusion matrix:\n", confusion_matrix(y_test, predictions))
