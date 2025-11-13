<<<<<<< HEAD
# NewsGuard AI 

**Streamlit app to analyze news articles for fake news, bias, sentiment, and more.**

This repository contains the initial scaffold for the NewsGuard AI group project (Phase 1).

## Project structure
See repository root for the full file and folder layout.

## Quick start (local)
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app/app.py`

## How to contribute
- Fork the repo and create a feature branch: `git checkout -b feature/your-model`
- Add your notebook under `/notebooks`
- Add your saved model under `/models`
- Add your prediction script under `/model_functions`
- Open a Pull Request to `main`

## Team Roles
- Team Lead: Onyeka Nwokike— sets up repo, trains topic model, integrates + deploys
- AI Model Developers: pick a model from the list in the project spec and add your work
=======
# 📰 NewsCheck AI

Streamlit app to analyze news articles for credibility, sentiment, clickbait, and more.
🔗 **Live App**: [https://newscheck-ai.streamlit.app/](https://newscheck-ai.streamlit.app/)

-----

## 👥 Contributors

  * **Onyeka Nwokike** — Team Lead / Topic Classification — [https://github.com/Nwokike](https://github.com/Nwokike)
  * **Stephen Ayankoso** — Fake News Detection — [https://github.com/Steve-ayan](https://github.com/Steve-ayan)
  * **Cleiton Langa** — Clickbait Detection — [https://github.com/cleitonlanga](https://github.com/cleitonlanga)
  * **Rivaldo** — Sentiment Analysis — [https://github.com/rivaldo56](https://github.com/rivaldo56)

-----

## 📘 Project Overview

**NewsCheck AI** is a modular NLP project built with Streamlit. Each team member contributed a trained model that analyzes different aspects of news articles. Incomplete modules display as “Coming Soon.”

-----

## 📁 Project Structure

```
newscheck-ai/
│
├── app.py
│
├── model_functions/
│   ├── topic.py
│   ├── fake.py
│   ├── sentiment.py
│   ├── clickbait.py
│   ├── bias.py         # Coming Soon
│   ├── summarizer.py   # Coming Soon
│   └── emotion.py      # Coming Soon
│
├── models/
│   ├── topic_model.pkl
│   ├── topic_vectorizer.pkl
│   ├── fake_news_model.pkl
│   ├── fake_news_vectorizer.pkl
│   ├── sentiment_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── clickbait_model.pkl
│   ├── clickbait_vectorizer.pkl
│   └── ...
│
├── notebooks/
│   ├── topic_classification.ipynb
│   ├── fake_news_training.ipynb
│   ├── sentiment_training.ipynb
│   ├── clickbait_training.ipynb
│   └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
```

-----

## 🧠 Models

This table shows the high-level status of each module. See the "Data Sources" section below for the specific datasets and requirements for each model.

| Feature | Function | Status |
| :--- | :--- | :---: |
| Topic Classification | `predict_topic(text)` | ✅ Done |
| Fake News Detection | `predict_fake(text)` | ✅ Done |
| Sentiment Analysis | `predict_sentiment(text)` | ✅ Done |
| Clickbait Detection | `is_clickbait(text)` | ✅ Done |
| Bias Detection | `detect_bias(text)` | 🚧 Coming Soon |
| Extractive Summarizer | `summarize(text)` | 🚧 Coming Soon |
| Emotion Detection | `get_emotion(text)` | 🚧 Coming Soon |

### Data Sources & Contributor Guide

This is the official list of datasets for the project. Contributors working on a "Coming Soon" module should use the specified dataset and deliverable.

  * **Topic Classification (Done)**

      * **Dataset:** [News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset)
      * **Deliverable:** A function `predict_topic(text)` in `model_functions/topic.py` that returns the predicted category as a string.

  * **Fake News Detection (Done)**

      * **Dataset:** [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
      * **Deliverable:** A function `predict_fake(text)` in `model_functions/fake.py` that returns a formatted string like `"High Risk (Fake) - 92.51%"`.

  * **Sentiment Analysis (Done)**

      * **Dataset:** [Sentiment Analysis for Financial News](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)
      * **Deliverable:** A function `predict_sentiment(text)` in `model_functions/sentiment.py` that returns "Positive," "Negative," or "Neutral."

  * **Clickbait Detection (Done)**

      * **Dataset:** [Clickbait Dataset](https://www.kaggle.com/datasets/amananandrai/clickbait-dataset)
      * **Deliverable:** A function `is_clickbait(headline_text)` in `model_functions/clickbait.py` that returns "Yes" or "No".

  * **Bias Detection (Coming Soon)**

      * **Dataset:** [MBIC: A Media Bias Annotation Dataset](https://www.kaggle.com/datasets/timospinde/mbic-a-media-bias-annotation-dataset)
      * **Deliverable:** A function `detect_bias(text)` in `model_functions/bias.py` that returns "Biased" or "Neutral."

  * **Extractive Summarizer (Coming Soon)**

      * **Dataset:** [Newspaper Text Summarization CNN/DailyMail](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail)
      * **Deliverable:** A function `summarize(text)` in `model_functions/summarizer.py` that returns a single string containing the 3-sentence summary.

  * **Emotion Detection (Coming Soon)**

      * **Dataset:** [Emotions Dataset for NLP](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)
      * **Deliverable:** A function `get_emotion(text)` in `model_functions/emotion.py` that returns the predicted emotion.

-----

## ⚙️ Quick Start

1.  Clone the repository:
    ```bash
    git clone https://github.com/Nwokike/newscheck-ai.git
    ```
2.  Navigate to the directory:
    ```bash
    cd newscheck-ai
    ```
3.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4.  Activate the environment:
      * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
      * **Windows:**
        ```bash
        venv\Scripts\activate
        ```
5.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6.  Run the app:
    ```bash
    streamlit run app.py
    ```

-----

## 🧩 Contributing

1.  Fork the repo and create a new feature branch:
    ```bash
    git checkout -b feature/your-model
    ```
2.  Add your files (see "Data Sources" section for model requirements):
      * Your training notebook $\rightarrow$ `/notebooks`
      * Your model + vectorizer $\rightarrow$ `/models`
      * Your inference script $\rightarrow$ `/model_functions`
3.  Push your branch and open a Pull Request to `main`.
>>>>>>> upstream/main
