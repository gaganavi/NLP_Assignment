import pandas as pd
import re
import nltk
import os
from nltk.corpus import stopwords
from datasets import load_dataset

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return ' '.join([word for word in text.split() if word not in stop_words])

def process_textbook_data(output_path):
    ds = load_dataset("open-phi/textbooks", split="train")
    df = ds.to_pandas()
    df.columns = df.columns.str.strip()

    # ✅ Use only existing columns
    df['topic'] = df['topic'].fillna('')
    df['concepts'] = df['concepts'].fillna('')
    df['outline'] = df['outline'].fillna('')
    df['markdown'] = df['markdown'].fillna('')

    # Combine all description fields
    df['combined'] = df['concepts'] + " " + df['outline'] + " " + df['markdown']
    df['combined'] = df['combined'].apply(clean_text)

    # Create output structure
    processed_books = [
        {"title": row['topic'], "description": row['combined']}
        for _, row in df.iterrows()
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pd.DataFrame(processed_books).to_json(output_path, orient='records', indent=2)
    print(f"✅ Processed data saved to {output_path}")
    print(df[['topic', 'combined']].head())

if __name__ == "__main__":
    process_textbook_data("data/books_metadata.json")
