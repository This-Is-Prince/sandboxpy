import csv
from collections import Counter
import re
from .utils import logger

class HeadlineAnalyzer:
    """Analyzes headlines and saves reports."""
    def __init__(self, articles):
        self.articles = articles

    def save_to_csv(self, filename):
        """Save the list of articles to a CSV file."""
        if not self.articles:
            return

        try:
            with open(filename, 'w', newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["title", "link"])
                writer.writeheader()
                writer.writerows(self.articles)
        except Exception as e:
            logger.error(f"An error occurred {e}")

    def generate_word_frequency_report(self, filename, top_n=20):
        """Analyzes word frequency and saves a report"""
        all_headlines = " ".join([article['title'] for article in self.articles])

        words = re.findall(r'\b\w+\b', all_headlines.lower())

        stop_words = {'a', 'an', 'the', 'and', 'in', 'of', 'to', 'for', 'is', 'on', 'with'}

        filtered_words = [word for word in words if word not in stop_words]

        word_counts = Counter(filtered_words)

        try:
            with open(filename, 'w', encoding="utf-8") as f:
                f.write("--- Top 20 Most Common Words in Headlines ---\n\n")
                for word, count in word_counts.most_common(top_n):
                    f.write(f"{word}: {count}\n")
        except Exception as e:
            logger.error(f"An error occurred {e}")