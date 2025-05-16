# 📚 Keyword-Based Textbook Retrieval (NLP Project)

This project is built for an NLP course assignment. It allows users to type in a keyword and get back the most relevant textbooks using TF-IDF and cosine similarity.


1. Clone the repository and navigate to the project:
   ```
   git clone <your-repo-url>
   cd NLP
   ```

3. Install requirements:
   ```
   pip install -r requirements.txt
   ```

4. Run preprocessing:
   ```
   python preprocessing/data_processing.py
   ```

5. Start the app using bash:
   ```
   cd C:\Users\gagan\Downloads\NLP_Project_openphi
streamlit run NLP/ui/app.py

   ```

Evaluation

The evaluation script supports basic Precision@K for ranked outputs.

Goal

To demonstrate:
- Preprocessing raw metadata
- Text similarity and document retrieval using TF-IDF
- A simple, interactive UI for NLP retrieval