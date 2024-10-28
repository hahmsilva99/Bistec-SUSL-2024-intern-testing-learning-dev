from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

# Log in with your token
login("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")

# Load model and tokenizer
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Use the model (e.g., for text generation)
input_text = "Hello, how are you?"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(inputs["input_ids"])

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
