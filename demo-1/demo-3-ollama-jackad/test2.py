# A list of hobbies or activities
hobbies = [
    "I like reading books",
    "I enjoy swimming in the pool",
    "I love hiking in the mountains",
    "I like painting landscapes",
    "I enjoy watching movies",
    "I like playing football with friends"
]

def jaccard_similarity(query, document):
    
    query = query.lower().split()
    document = document.lower().split()
    
    
    intersection = set(query).intersection(set(document))
    
    
    union = set(query).union(set(document))
    
    
    return len(intersection) / len(union)

def find_most_similar_hobby(user_input, hobbies):
    similarities = []  

    for hobby in hobbies:
        similarity = jaccard_similarity(user_input, hobby)
        similarities.append(similarity)
    
    
    most_similar_hobby = hobbies[similarities.index(max(similarities))]
    
    return most_similar_hobby

user_input = input("What is your favorite hobby? ")


similar_hobby = find_most_similar_hobby(user_input, hobbies)


print(f"Based on your input, a similar hobby is: {similar_hobby}")
