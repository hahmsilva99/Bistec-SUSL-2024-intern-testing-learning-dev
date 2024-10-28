from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("i hate this place")
print(result)
