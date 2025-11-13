<<<<<<< HEAD
import streamlit as st
import importlib
from pathlib import Path
import traceback

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="NewsGuard AI",
    page_icon="📰",
    layout="wide"
)

st.title("📰 NewsGuard AI")
st.caption("Empowering readers with AI-driven news credibility analysis")

st.markdown(
    """
    **Welcome!**  
    Paste any news article below and our AI models will analyze it for:
    - 🧩 **Topic Classification**  
    - ⚠️ **Fake News Detection**  
    - 💬 **Sentiment Analysis**  
    - 🎯 **Clickbait Detection**  
    - 🧠 **Bias Detection**  
    - ✂️ **Summarization**  
    - ❤️ **Emotion Detection**  
    """
)

# -----------------------------
# Input Section
# -----------------------------
text = st.text_area("📄 Paste your news article here:", height=250, placeholder="Enter or paste your news article text...")

# Sidebar configuration
st.sidebar.header("⚙️ Options")
show_topic = st.sidebar.checkbox("Show Topic Classification", value=True)
show_fake = st.sidebar.checkbox("Show Fake News Detection", value=True)
show_sentiment = st.sidebar.checkbox("Show Sentiment Analysis", value=True)
show_clickbait = st.sidebar.checkbox("Show Clickbait Detection", value=False)
show_bias = st.sidebar.checkbox("Show Bias Detection", value=False)
show_summarizer = st.sidebar.checkbox("Show Summarizer", value=False)
show_emotion = st.sidebar.checkbox("Show Emotion Detection", value=False)

# -----------------------------
# Utility Functions
# -----------------------------
def safe_import_and_call(module_path: str, func_name: str, *args):
    """
    Tries to import a model function dynamically and execute it.
    Returns 'Coming Soon' if module or function not found or raises error.
    """
    try:
        module = importlib.import_module(module_path)
        func = getattr(module, func_name)
        return func(*args)
    except Exception as e:
        error_type = type(e).__name__
        return f"🚧 Coming Soon — {error_type}"

def display_card(title: str, result: str, icon: str):
    """Pretty result card"""
    st.markdown(
        f"""
        <div style='background-color:#f8f9fa;padding:1.2rem;border-radius:1rem;margin-bottom:1rem;
                    box-shadow:0 1px 4px rgba(0,0,0,0.1)'>
            <h4 style='margin-bottom:0.5rem;'>{icon} {title}</h4>
            <p style='font-size:1.1rem;margin:0;'>{result}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Run Analysis
# -----------------------------
if st.button("🔍 Analyze Article", use_container_width=True):
    if not text.strip():
        st.warning("⚠️ Please paste a news article before analyzing.")
    else:
        st.subheader("📊 Analysis Results")

        col1, col2 = st.columns(2)

        # LEFT COLUMN MODELS
        with col1:
            if show_topic:
                res = safe_import_and_call("model_functions.topic", "predict_topic", text)
                display_card("Topic Classification", res, "🧩")

            if show_fake:
                res = safe_import_and_call("model_functions.fake", "predict_fake", text)
                display_card("Fake News Detection", res, "⚠️")

            if show_sentiment:
                res = safe_import_and_call("model_functions.sentiment", "predict_sentiment", text)
                display_card("Sentiment Analysis", res, "💬")

        # RIGHT COLUMN MODELS
        with col2:
            if show_clickbait:
                headline = text.strip().split("\\n")[0]
                res = safe_import_and_call("model_functions.clickbait", "is_clickbait", headline)
                display_card("Clickbait Detection", res, "🎯")

            if show_bias:
                res = safe_import_and_call("model_functions.bias", "detect_bias", text)
                display_card("Bias Detection", res, "🧠")

            if show_summarizer:
                res = safe_import_and_call("model_functions.summarizer", "summarize", text)
                display_card("Summarizer", res, "✂️")

            if show_emotion:
                res = safe_import_and_call("model_functions.emotion", "get_emotion", text)
                display_card("Emotion Detection", res, "❤️")

        st.success("✅ Analysis complete!")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <hr>
    <small>
    © 2025 NewsGuard AI Team — Licensed under the Apache License 2.0.  
    Contribute or fork at 
    <a href="https://github.com/Nwokike/newsguard-ai" target="_blank">github.com/Nwokike/newsguard-ai</a>.
    </small>
    """,
    unsafe_allow_html=True,
)
=======
import streamlit as st
import importlib
from pathlib import Path
import traceback

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="NewsCheck AI",
    page_icon="📰",
    layout="wide"
)

st.title("📰 NewsCheck AI")
st.caption("Empowering readers with AI-driven news credibility analysis")

st.markdown(
    """
    **Welcome!** Paste any news article below and our AI models will analyze it for:
    - 🧩 **Topic Classification** - ⚠️ **Fake News Detection** - 💬 **Sentiment Analysis** - 🎯 **Clickbait Detection** - 🧠 **Bias Detection** - ✂️ **Summarization** - ❤️ **Emotion Detection** """
)

# -----------------------------
# Input Section
# -----------------------------
text = st.text_area("📄 Paste your news article here:", height=250, placeholder="Enter or paste your news article text...")

# Sidebar configuration
st.sidebar.header("⚙️ Options")
show_topic = st.sidebar.checkbox("Show Topic Classification", value=True)
show_fake = st.sidebar.checkbox("Show Fake News Detection", value=True)
show_sentiment = st.sidebar.checkbox("Show Sentiment Analysis", value=True)
show_clickbait = st.sidebar.checkbox("Show Clickbait Detection", value=False)
show_bias = st.sidebar.checkbox("Show Bias Detection", value=False)
show_summarizer = st.sidebar.checkbox("Show Summarizer", value=False)
show_emotion = st.sidebar.checkbox("Show Emotion Detection", value=False)

# -----------------------------
# Utility Functions
# -----------------------------
def safe_import_and_call(module_path: str, func_name: str, *args):
    """
    Tries to import a model function dynamically and execute it.
    Returns 'Coming Soon' if module or function not found or raises error.
    """
    try:
        module = importlib.import_module(module_path)
        func = getattr(module, func_name)
        return func(*args)
    except Exception as e:
        error_type = type(e).__name__
        return f"🚧 Coming Soon — {error_type}"

def display_card(title: str, result: str, icon: str):
    """Pretty result card"""
    st.markdown(
        f"""
        <div style='background-color:#f8f9fa;padding:1.2rem;border-radius:1rem;margin-bottom:1rem;
                    box-shadow:0 1px 4px rgba(0,0,0,0.1)'>
            <h4 style='margin-bottom:0.5rem;'>{icon} {title}</h4>
            <p style='font-size:1.1rem;margin:0;'>{result}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Run Analysis
# -----------------------------
if st.button("🔍 Analyze Article", use_container_width=True):
    if not text.strip():
        st.warning("⚠️ Please paste a news article before analyzing.")
    else:
        st.subheader("📊 Analysis Results")

        col1, col2 = st.columns(2)

        # LEFT COLUMN MODELS
        with col1:
            if show_topic:
                res = safe_import_and_call("model_functions.topic", "predict_topic", text)
                display_card("Topic Classification", res, "🧩")

            if show_fake:
                res = safe_import_and_call("model_functions.fake", "predict_fake", text)
                display_card("Fake News Detection", res, "⚠️")

            if show_sentiment:
                res = safe_import_and_call("model_functions.sentiment", "predict_sentiment", text)
                display_card("Sentiment Analysis", res, "💬")

        # RIGHT COLUMN MODELS
        with col2:
            if show_clickbait:
                headline = text.strip().split("\n")[0]
                res = safe_import_and_call("model_functions.clickbait", "is_clickbait", headline)
                display_card("Clickbait Detection", res, "🎯")

            if show_bias:
                res = safe_import_and_call("model_functions.bias", "detect_bias", text)
                display_card("Bias Detection", res, "🧠")

            if show_summarizer:
                res = safe_import_and_call("model_functions.summarizer", "summarize", text)
                display_card("Summarizer", res, "✂️")

            if show_emotion:
                res = safe_import_and_call("model_functions.emotion", "get_emotion", text)
                display_card("Emotion Detection", res, "❤️")

        st.success("✅ Analysis complete!")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <hr>
    <small>
    © 2025 NewsCheck AI Team — Licensed under the Apache License 2.0.  
    Contribute or fork at 
    <a href="https://github.com/Nwokike/newscheck-ai" target="_blank">github.com/Nwokike/newscheck-ai</a>.
    </small>
    """,
    unsafe_allow_html=True,
)
>>>>>>> upstream/main
