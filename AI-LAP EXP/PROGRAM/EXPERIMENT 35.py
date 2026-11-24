
# Import required libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load Breast Cancer dataset
data = datasets.load_breast_cancer()

# Select two classes and features
X = data.data[:, :2]
y = data.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create SVM model
model = SVC(kernel='linear')

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Display results
print("SVM Binary Classification")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Predict a new sample
sample = [[15.0, 20.0]]
prediction = model.predict(sample)

print("New Sample Prediction:",
      data.target_names[prediction[0]])
