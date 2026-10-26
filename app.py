
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Question Answering with Transformers",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Question Answering with Transformers")
st.write(
    "Enter a passage and ask a question. "
    "The AI model will extract an answer from the passage."
)

@st.cache_resource
def load_qa_model():
    return pipeline(
        "question-answering",
        model="distilbert/distilbert-base-cased-distilled-squad"
    )

context = st.text_area(
    "Context passage",
    height=220,
    placeholder="Paste a paragraph or passage here..."
)

question = st.text_input(
    "Your question",
    placeholder="What would you like to know?"
)

if st.button("Get Answer", type="primary"):
    if not context.strip() or not question.strip():
        st.warning("Please enter both a context passage and a question.")
    else:
        with st.spinner("Finding the answer..."):
            qa_model = load_qa_model()
            result = qa_model(
                question=question,
                context=context
            )

        st.subheader("Predicted Answer")
        st.success(result["answer"])

        st.metric(
            "Model Confidence",
            f"{result['score']:.1%}"
        )

        st.caption(
            "The confidence score is a model score, "
            "not a guarantee that the answer is correct."
        )
