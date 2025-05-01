# app.py

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re

# Set of English stop words
stop_words = set(stopwords.words('english'))

st.title("🧠 NLP Word Cloud Generator with Text Stats")

user_text = st.text_area("Enter your text here:")

# Clean and process text
def preprocess_text(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())  # Extract only words
    filtered_words = [word for word in words if word not in stop_words]
    return words, filtered_words

if user_text.strip():
    # Raw text stats
    total_chars = len(user_text)
    total_words_raw, filtered_words = preprocess_text(user_text)
    total_words = len(total_words_raw)
    total_unique_words = len(set(total_words_raw))
    total_filtered = len(filtered_words)

    st.subheader("📊 Text Statistics:")
    st.write(f"📝 Total Characters: {total_chars}")
    st.write(f"🔢 Total Words (before stop word removal): {total_words}")
    st.write(f"🔠 Unique Words: {total_unique_words}")
    st.write(f"❌ Words After Stop Word Removal: {total_filtered}")

    if st.button("Generate Word Cloud"):
        if total_filtered == 0:
            st.warning("After removing stop words, no words remain to display.")
        else:
            clean_text = ' '.join(filtered_words)
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(clean_text)

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
else:
    st.info("Please enter some text to see stats and generate a word cloud.")
