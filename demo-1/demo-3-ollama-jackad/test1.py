# Define the corpus of activities
corpus_of_activities = [
    "Go for a run and boost your fitness level.",
    "Take a relaxing walk on the beach and watch the sunset.",
    "Attend a painting class and explore your artistic side.",
    "Enjoy a weekend camping trip and reconnect with nature.",
    "Try a cooking class and learn to make your favorite dishes.",
    "Visit a botanical garden and appreciate the beauty of nature.",
    "Sign up for a dance class and learn a new style.",
    "Participate in a book club and discuss your favorite reads.",
    "Explore a new city and experience its culture and cuisine.",
    "Take a pottery class and create something with your hands."
]

# Define the Jaccard similarity function
def jaccard_similarity(query, document):
    query = query.lower().split(" ")  # Convert the query to lowercase and split into words
    document = document.lower().split(" ")  # Convert the document to lowercase and split into words
    
    intersection = set(query).intersection(set(document))  # Find common words between query and document
    union = set(query).union(set(document))  # Find all unique words
    
    return len(intersection) / len(union)  # Return Jaccard similarity score (intersection/union)

# Function to return the most similar document
def return_response(query, corpus):
    similarities = []  # Empty list to store similarity scores
    
    for doc in corpus:  # Loop through each document in the corpus
        similarity = jaccard_similarity(query, doc)  # Compute the similarity between query and document
        similarities.append(similarity)  # Store the similarity score
    
    return corpus[similarities.index(max(similarities))]  # Return the most similar document

# Example interaction
user_prompt = "What kind of leisure activity do you enjoy?"
user_input = "I enjoy nature walks"

# Get the most similar activity based on the user's input
response = return_response(user_input, corpus_of_activities)
print(f"Suggested activity: {response}")
