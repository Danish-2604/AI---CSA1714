
from textblob import TextBlob

# Get input from the user
text = input("Enter a sentence: ")

# Perform sentiment analysis
analysis = TextBlob(text)

# Calculate polarity
polarity = analysis.sentiment.polarity

# Classify sentiment
if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Display results
print("\nSentiment Analysis Result")
print("Text:", text)
print("Polarity Score:", polarity)
print("Sentiment:", sentiment)
