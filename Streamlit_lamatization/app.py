# app.py

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re

# Hardcoded English stop words list (safe for deployment)
STOP_WORDS = set("""
a about above after again against all am an and any are as at be because been before being below between both but by
could did do does doing down during each few for from further had has have having he he'd he'll he's her here here's hers
herself him himself his how how's i i'd i'll i'm i've if in into is it it's its itself let's me more most my myself nor of
on once only or other ought our ours ourselves out over own same she she'd she'll she's should so some such than that
that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to
too under until up very was we we'd we'll we're we've were what what's when when's where where's which while who who's whom
why why's with would you you'd you'll you're you've your yours yourself yourselves
""".split())

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
