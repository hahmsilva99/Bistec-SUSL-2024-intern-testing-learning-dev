from transformers import pipeline
classifier = pipeline('sentiment-analysis')
result = classifier("I've been waiting for this tutorial my whole life!")
print(result)
