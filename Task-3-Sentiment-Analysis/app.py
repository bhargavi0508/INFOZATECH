
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis Tool",
    page_icon="💬",
    layout="centered"
)

# Application title
st.title("💬 Sentiment Analysis Tool")
st.write(
    "Analyze the sentiment of a sentence, product review, "
    "or customer feedback using AI."
)

st.divider()

# Text input
user_text = st.text_area(
    "Enter your text:",
    placeholder="Example: This product is amazing! I really love it.",
    height=150
)

# Analyze button
if st.button("🔍 Analyze Sentiment", use_container_width=True):

    if user_text.strip():

        # Calculate sentiment scores
        scores = analyzer.polarity_scores(user_text)
        compound_score = scores["compound"]

        # Determine sentiment
        if compound_score >= 0.05:
            sentiment = "Positive 😊"
            st.success(f"Sentiment: {sentiment}")

        elif compound_score <= -0.05:
            sentiment = "Negative 😞"
            st.error(f"Sentiment: {sentiment}")

        else:
            sentiment = "Neutral 😐"
            st.info(f"Sentiment: {sentiment}")

        # Display results
        st.subheader("📊 Sentiment Analysis Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Overall Sentiment", sentiment)

        with col2:
            st.metric("Compound Score", f"{compound_score:.3f}")

        st.write("### Individual Scores")

        st.progress(scores["pos"], text=f"Positive: {scores['pos']:.2%}")
        st.progress(scores["neu"], text=f"Neutral: {scores['neu']:.2%}")
        st.progress(scores["neg"], text=f"Negative: {scores['neg']:.2%}")

        with st.expander("What do these scores mean?"):
            st.write(
                "Positive, Neutral, and Negative scores indicate "
                "the proportions associated with each sentiment. "
                "The compound score ranges from -1 (most negative) "
                "to +1 (most positive)."
            )

    else:
        st.warning("Please enter some text before analyzing.")

st.divider()
st.caption("InfozaTech AI Internship | Task 3: Sentiment Analysis")
