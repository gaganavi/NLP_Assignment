def evaluate_precision_at_k(predicted_titles, relevant_titles, k=5, verbose=True):
    if k == 0:
        return 0.0
    k = min(k, len(predicted_titles))  # Prevent index out of bounds
    predicted_top_k = predicted_titles[:k]
    relevant_set = set(title.lower() for title in relevant_titles)  # case-insensitive match
    correct = sum(1 for title in predicted_top_k if title.lower() in relevant_set)
    precision = correct / k

    if verbose:
        print(f"Predicted Top-{k}: {predicted_top_k}")
        print(f"Relevant Titles: {relevant_titles}")
        print(f"Matches: {correct} / {k}")
        print(f"Precision@{k}: {precision:.2f}")
    
    return precision

if __name__ == "__main__":
    predicted = ["AI Basics", "ML Guide", "Deep Learning Book", "NLP Mastery", "Transformers Explained"]
    relevant = ["Deep Learning Book", "NLP Mastery", "Transformers Explained"]
    evaluate_precision_at_k(predicted, relevant, k=5)
