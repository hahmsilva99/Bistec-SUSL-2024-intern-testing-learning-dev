from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Step 1: Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased')

# Step 2: Tokenize the input text
inputs = tokenizer("I love learning new things!", return_tensors="pt")

# Step 3: Get model predictions
outputs = model(**inputs)

# Step 4: Print the raw output (logits)
print(outputs)
