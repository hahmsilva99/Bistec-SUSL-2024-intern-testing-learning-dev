from transformers import pipeline

classifier = pipeline("sentiment-analysis")
output = classifier("i hate my mind")

print(output)