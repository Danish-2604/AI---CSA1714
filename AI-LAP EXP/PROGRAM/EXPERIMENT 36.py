
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensions to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Display original and reduced dimensions
print("Original Dataset Shape:", X.shape)
print("Reduced Dataset Shape:", X_pca.shape)

# Display explained variance
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Visualize PCA results
plt.figure(figsize=(8, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1],
            c=y, cmap='viridis')

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Dimensionality Reduction Using PCA")
plt.colorbar(label="Iris Classes")
plt.show()
