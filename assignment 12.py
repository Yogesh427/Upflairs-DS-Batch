"""
Assignment 12 - Decision Trees, Random Forest & Naive Bayes
"""

# Q1
print("Q1. Decision Tree")
print("""A Decision Tree is a supervised machine learning algorithm used for
classification and regression. It splits data into branches based on feature
values until a decision (class) is reached. For classification, the model
chooses the best feature using Gini Index or Entropy and predicts the class
label at the leaf node.""")

# Q2
print("\nQ2. Difference between Decision Tree and Random Forest")
print("""
Decision Tree:
- Single tree
- Faster to train
- Can overfit
- Lower accuracy on complex data

Random Forest:
- Collection of many decision trees
- More accurate
- Reduces overfitting
- Slightly slower
""")

# Q3
print("Q3. Naive Bayes & Bayes Theorem")
print("""
Naive Bayes is a probabilistic classifier based on Bayes Theorem.
Bayes Theorem:
P(A|B) = (P(B|A) * P(A)) / P(B)

Example:
If an email contains the word 'Offer', Naive Bayes estimates the probability
that it is Spam or Not Spam and predicts the class with the higher probability.
""")

# Q4
print("Q4. Spam Classification")
spam = 3
notspam = 3
offer_given_spam = 3/3
offer_given_notspam = 0/3
p_spam = (offer_given_spam * (spam/6))
p_notspam = (offer_given_notspam * (notspam/6))
print("P(Spam|Offer) =", p_spam)
print("P(Not Spam|Offer) =", p_notspam)
print("Prediction: Spam")

# Q5
print("\nQ5. Iris Dataset - Decision Tree")
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

X = df.iloc[:, :-1]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))
print("Accuracy:", accuracy_score(y_test, pred))

# Q6
print("\nQ6. Titanic Dataset - Random Forest")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

try:
    df = pd.read_csv("Titanic.csv")   # place Titanic.csv in same folder
    df["Age"].fillna(df["Age"].median(), inplace=True)
    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
    df["Sex"] = df["Sex"].map({"male":0,"female":1})
    df["Embarked"] = df["Embarked"].map({"S":0,"C":1,"Q":2})

    X = df[["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
    y = df["Survived"]

    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.2,random_state=42)

    rf=RandomForestClassifier(random_state=42)
    rf.fit(X_train,y_train)
    pred=rf.predict(X_test)

    print(classification_report(y_test,pred))
    print("Accuracy:",accuracy_score(y_test,pred))
except FileNotFoundError:
    print("Titanic.csv not found. Download Titanic dataset and keep it in the same folder.")
