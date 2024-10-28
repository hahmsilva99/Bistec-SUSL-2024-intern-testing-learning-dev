from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
output = generator("In this course, we will teach you", max_length=50, pad_token_id=generator.tokenizer.eos_token_id)
print(output)

