import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re

# Download stopwords if not already available
nltk.download('stopwords')

# Set of English stop words
stop_words = set(stopwords.words('english'))

# App title
st.title("🧠 NLP Word Cloud Generator")

# User input
user_text = st.text_area("Enter your text here:")

# Clean and process text
def preprocess_text(text):
    # Lowercase and remove non-alphabetic characters
    words = re.findall(r'\b[a-z]+\b', text.lower())
    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Button to generate word cloud
if st.button("Generate Word Cloud"):
    if user_text.strip() == "":
        st.warning("Please enter some text to generate the word cloud.")
    else:
        clean_text = preprocess_text(user_text)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(clean_text)

        # Display the image
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)


