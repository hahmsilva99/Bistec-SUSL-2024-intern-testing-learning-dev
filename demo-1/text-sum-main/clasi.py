from transformers import pipeline

classifier = pipeline("zero-shot-classification")
output = classifier (
    "this is about calassification",
    candidate_labels=["education", "agriculture","bussiness"]
)

print(output)
