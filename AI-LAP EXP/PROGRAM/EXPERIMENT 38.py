
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create sample dataset
X = np.array([
    [1, 2], [2, 3], [3, 2],
    [8, 8], [9, 8], [8, 9],
    [1, 8], [2, 9], [3, 8]
])

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# Get cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Display cluster results
print("Cluster Labels:")
print(labels)

print("\nCluster Centroids:")
print(centroids)

# Visualize clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis',
            s=100, label='Data Points')

plt.scatter(centroids[:, 0], centroids[:, 1],
            color='red', marker='X', s=200,
            label='Centroids')

plt.title("K-Means Clustering")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
