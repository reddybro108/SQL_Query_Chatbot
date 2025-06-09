import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)


def extract_keywords(text: str) -> set:
    """
    Extract relevant keywords from text for SQL query generation.

    Args:
        text: Input text string.

    Returns:
        Set of keywords excluding stopwords.
    """
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text.lower())
    keywords = {word for word in tokens if word.isalnum() and word not in stop_words}
    return keywords
