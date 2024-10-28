from transformers import pipeline

# Use a different model for sentiment analysis
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Run sentiment analysis
result = classifier("I love learning about new technology!")
print(result)
