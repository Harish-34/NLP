from sklearn.feature_extraction.text import CountVectorizer

sentence = "data science and ai genai has great career ahead data"
vectorizer = CountVectorizer()
vector = vectorizer.fit_transform([sentence])
vector.toarray()