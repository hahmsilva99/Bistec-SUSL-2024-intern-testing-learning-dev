from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# List of activities (documents) to compare against the query
activities = [
    "Go for a walk in the park.",
    "Visit a museum to learn something new.",
    "Attend a concert and enjoy live music.",
    "Go hiking in the mountains.",
    "Have a picnic with your friends.",
    "Try a new restaurant with exotic cuisine.",
    "Join a yoga class to relax your mind and body.",
    "Play a sport with friends for some fun exercise.",
    "Attend a workshop to learn new skills.",
    "Visit an amusement park for thrilling rides."
]

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert each activity into a numerical embedding
activity_embeddings = model.encode(activities)

# User input
user_query = "I want to go hiking outdoors."

# Convert the user's query into an embedding
query_embedding = model.encode([user_query])

# Calculate cosine similarity between the query and all activities
similarities = cosine_similarity(query_embedding, activity_embeddings)

# Get the index and similarity scores, sort by the highest score
indexed_scores = list(enumerate(similarities[0]))
sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)

# Display the most similar activities
print("Most similar activities to your query:")
for index, score in sorted_scores:
    if score > 0.3:  # Only show results with a score above 0.3
        print(f"Similarity: {score:.2f} - Activity: {activities[index]}")
