import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(path):
    with open(path, 'r') as f:
        return json.load(f)

def tfidf_ranking(query, books, top_k=5):
    corpus = [book['description'] for book in books]
    titles = [book['title'] for book in books]
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(corpus + [query])
    cosine_sim = cosine_similarity(X[-1], X[:-1])
    scores = cosine_sim.flatten()
    top_indices = scores.argsort()[::-1][:top_k]
    return [(titles[i], scores[i]) for i in top_indices]