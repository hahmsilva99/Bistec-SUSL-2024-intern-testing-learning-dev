from transformers import pipeline

classifier = pipeline("zero-shot-classification")
result = classifier("This is an educational video", candidate_labels=["education", "politics", "business"])
print(result)
