
# Import required libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Create user-item rating dataset
data = {
    'Movie1': [5, 4, 0, 0, 2],
    'Movie2': [4, 5, 0, 2, 0],
    'Movie3': [0, 0, 5, 4, 4],
    'Movie4': [0, 2, 4, 5, 5]
}

# Create DataFrame
df = pd.DataFrame(data, index=[
    'User1', 'User2', 'User3', 'User4', 'User5'
])

print("User Ratings:")
print(df)

# Calculate user similarity
similarity = cosine_similarity(df)
similarity_df = pd.DataFrame(
    similarity,
    index=df.index,
    columns=df.index
)

print("\nUser Similarity:")
print(similarity_df.round(2))

# Select target user
target_user = 'User1'

# Calculate recommendations
user_sim = similarity_df.loc[target_user].drop(target_user)

# Predict ratings for unrated movies
recommendations = {}

for movie in df.columns:
    if df.loc[target_user, movie] == 0:
        numerator = sum(
            user_sim[user] * df.loc[user, movie]
            for user in user_sim.index
        )

        denominator = sum(
            abs(user_sim[user])
            for user in user_sim.index
            if df.loc[user, movie] > 0
        )

        if denominator > 0:
            recommendations[movie] = numerator / denominator

# Display recommendations
print("\nRecommended Movies for", target_user)

for movie, rating in sorted(
    recommendations.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(movie, "Predicted Rating:", round(rating, 2))
