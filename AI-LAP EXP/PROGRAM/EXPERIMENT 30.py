
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample dataset
X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])

Y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict values
Y_pred = model.predict(X_test)

# Display results
print("Actual Values:", Y_test)
print("Predicted Values:", Y_pred)

# Calculate Mean Squared Error
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)

# Predict a new value
new_value = np.array([[11]])
prediction = model.predict(new_value)

print("Prediction for input 11:", prediction[0])
