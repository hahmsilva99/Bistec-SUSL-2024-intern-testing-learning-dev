import requests

# Update the API URL and token
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    # Sending a POST request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Return the response in JSON format
    return response.json()

# Sample input data to be sent to the model
data = query({"inputs": "Can you explain Hugging Face API?"})

# Print the response from the API
print(data)

