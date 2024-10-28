from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# New set of activities (documents)
activities = [
    "Take a bike ride along the river and enjoy the view.",
    "Watch a movie at the cinema and relax.",
    "Go camping and experience the beauty of nature.",
    "Play basketball with your friends for some fun exercise.",
    "Try a new recipe and cook a delicious meal at home.",
    "Attend a painting class and unleash your creativity.",
    "Go kayaking and feel the thrill of adventure.",
    "Join a book club and discuss your favorite reads.",
    "Go stargazing and appreciate the night sky.",
    "Visit a zoo and learn about different animals."
]

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert the activities to embeddings
activity_embeddings = model.encode(activities)

# Define a user's query
query = "What's a fun outdoor activity?"

# Convert the query into an embedding
query_embedding = model.encode([query])

# Calculate cosine similarity between the query and the activity embeddings
similarity_scores = cosine_similarity(query_embedding, activity_embeddings)

# Enumerate and sort the results by similarity score
indexed_scores = list(enumerate(similarity_scores[0]))
sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)

# Print the most similar activities
recommended_activities = []
for index, score in sorted_scores:
    formatted_score = "{:.2f}".format(score)
    print(f"{formatted_score} => {activities[index]}")
    
    # Add only activities with a score higher than 0.3 to recommendations
    if score > 0.3:
        recommended_activities.append(activities[index])
