
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Chatbot ka title
st.title("🤖 FAQ Chatbot")
st.write("Ask me a question about our services!")

# FAQ data: questions aur answers
faqs = [
    {
        "question": "What are your working hours?",
        "answer": "Our working hours are Monday to Friday, 9 AM to 5 PM."
    },
    {
        "question": "How can I contact support?",
        "answer": "You can contact our support team at support@example.com."
    },
    {
        "question": "What services do you offer?",
        "answer": "We offer web development, AI solutions, and digital marketing."
    },
    {
        "question": "How can I apply for an internship?",
        "answer": "You can apply by visiting our official internship application page."
    },
    {
        "question": "Is the internship free?",
        "answer": "Please check the official internship announcement for fee details."
    },
    {
        "question": "How do I submit my project?",
        "answer": "Follow the official internship instructions for project submission."
    }
]

# Questions ki list
questions = [faq["question"] for faq in faqs]

# Text ko numerical features mein convert karna
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])

    # User question aur FAQs ki similarity compare karna
    scores = cosine_similarity(user_vector, question_vectors)[0]

    best_match_index = scores.argmax()
    best_score = scores[best_match_index]

    # Agar match kamzor ho, to fallback message
    if best_score < 0.20:
        return (
            "Sorry, I couldn't find a suitable answer. "
            "Please try another question."
        )

    return faqs[best_match_index]["answer"]


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani conversation show karna
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User ka question
user_question = st.chat_input("Type your question here...")

if user_question:
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.write(user_question)

    answer = get_answer(user_question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)
