from transformers import pipeline

question = pipeline("question-answering")
output = question(
    question="where do i work",
    context=" my name is harshana , iwork from sabaragamuwa university of sri lanka"
)

print(output)