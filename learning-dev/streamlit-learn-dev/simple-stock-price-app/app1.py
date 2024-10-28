import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

st.markdown("""
<style>
 .st-emotion-cache-h4xjwg(
            visibility:hidden;
            )           
            
            
</style>

""",unsafe_allow_html=True)

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.write(fig)  # Renders a Matplotlib plot

data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.write(data)  # Renders as an interactive table

st.write("Hello, Streamlit!")  # Displays plain text
st.write("# Header 1\nThis is **bold** text.")  # Renders as Markdown
