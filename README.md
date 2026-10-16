# FAQ Chatbot

## Project Overview
This project is a simple FAQ Chatbot built using Python, Streamlit, and Scikit-learn. It answers frequently asked questions by comparing the user's question with a predefined FAQ dataset.

## Features
- Interactive chat interface
- Predefined questions and answers
- TF-IDF text vectorization
- Cosine similarity for question matching
- Fallback response for questions without a suitable match
- Chat history during the active session

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Cosine Similarity

## Installation

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Install the required libraries:

   `python -m pip install -r requirements.txt`

4. Run the application:

   `python -m streamlit run app.py`

5. Open the local URL displayed in your terminal.

## How It Works
The chatbot converts stored FAQ questions into TF-IDF vectors. When a user submits a question, it compares that question with the stored questions using cosine similarity and returns the answer associated with the best match if the similarity score meets the configured threshold.

## Limitations
The chatbot uses a predefined FAQ dataset. It does not generate answers independently and may not understand questions outside its stored knowledge.

## Future Improvements
- Expand the FAQ dataset
- Improve question matching
- Add more customizable responses
- Improve the user interface

## Author
Umar Abid
