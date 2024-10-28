import streamlit as st

# Sample JSON data
data = {
    "name": "Alice",
    "age": 30,
    "location": {
        "city": "New York",
        "state": "NY"
    },
    "hobbies": ["Reading", "Hiking", "Coding"]
}

# Display JSON in the Streamlit app
st.json(data, expanded=True)
