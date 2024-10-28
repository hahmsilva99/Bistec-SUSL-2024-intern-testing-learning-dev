from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from cv_data import cv_data

app = Flask(__name__)

# Load Microsoft DialoGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Filter candidates by skill
def filter_candidates_by_skill(skill):
    matching_candidates = []
    for name, details in cv_data.items():
        if skill.lower() in [s.lower() for s in details['skills']]:
            matching_candidates.append(name)
    return matching_candidates

# Query CV data
def query_cv(candidate_name, query_type):
    if candidate_name in cv_data:
        cv = cv_data[candidate_name]
        
        if query_type == "skills":
            return f"Skills: {', '.join(cv['skills'])}"
        elif query_type == "experience":
            exp_details = "\n".join([f"{exp['position']} at {exp['company']} ({exp['years']} years)" for exp in cv['experience']])
            return f"Experience: \n{exp_details}"
        elif query_type == "education":
            edu = cv['education']
            return f"Education: {edu['degree']} from {edu['university']} (Graduated in {edu['graduation_year']})"
        elif query_type == "contact":
            contact = cv.get('contact', 'No contact details available.')
            return f"Contact Details: {contact}"
        else:
            return "Invalid query type."
    else:
        return "Candidate not found."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['query']
    
    # Filter candidates by the skill mentioned
    matching_candidates = filter_candidates_by_skill(user_input)
    
    if matching_candidates:
        return jsonify({'candidates': matching_candidates})
    else:
        return jsonify({'response': "No person with the relevant skill is mentioned in our data."})

@app.route('/details', methods=['POST'])
def details():
    data = request.json
    candidate_name = data['candidate']
    detail_type = data['detail']
    
    # Query the selected candidate's details
    detail_response = query_cv(candidate_name, detail_type)
    
    return jsonify({'response': detail_response})

if __name__ == '__main__':
    app.run(debug=True)
