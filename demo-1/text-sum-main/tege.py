from transformers import pipeline

generator = pipeline("text-generation")
output = generator("i want to be succesfull man in ai technologies")



print( output )

classification = pipeline("text-generation",model="distilgpt2")

result= classification(
    "i want be good software engineer at ai",
    max_length=30,
    num_return_sequences=2,
)

print(result)
