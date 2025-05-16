import streamlit as st
import sys
import os

# Add the root of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from NLP.ranking.tfidf_ranker import load_data, tfidf_ranking



st.title("📚 Keyword-Based Textbook Finder")

query = st.text_input("Enter a keyword or topic:")
if query:
    books = load_data("data/books_metadata.json")
    results = tfidf_ranking(query, books)
    st.subheader("Top Matches:")
    for title, score in results:
        st.markdown(f"**{title}** — Relevance Score: `{score:.4f}`")