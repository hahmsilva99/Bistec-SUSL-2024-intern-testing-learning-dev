"""import os
from dotenv import load_dotenv


import requests

load_dotenv()

api_token = os.getenv("API_Token")


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {api_token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
})


print(output) """

from transformers import pipeline
from huggingface_hub import login

# Replace with your actual Hugging Face API token
API_Token = "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"

# Log in with the correct API token
login(API_Token)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input paragraph for summarization
output = summarizer(
    "A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). "
    "Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, "
    "particularly journalistic styles, a paragraph can be just one sentence long."
)

# Print the summarized output
print(output)
