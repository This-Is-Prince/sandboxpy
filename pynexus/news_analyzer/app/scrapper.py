import requests
from bs4 import BeautifulSoup
from .exceptions import ScrappingError
from .utils import logger

class NewsScrapper:
    """Scrapes news headlines from a given URL."""
    def __init__(self, url):
        self.url = url
        self.articles = []

    def _fetch_page(self):
        """Fetches the webpage content."""
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching the URL: {e}")
            raise ScrappingError(f"Could not fetch data from {self.url}") from e
        
    def _parse_content(self, html_content):
        """A GENERATOR that parses HTML and yields structured article data."""
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            headlines = soup.find_all('h2')

            for headline in headlines:
                title = headline.get_text(strip=True)
                link_tag = headline.find_parent('a')
                link = link_tag['href'] if link_tag else "No link found"
                if not link.startswith('http'):
                    link = "https://www.bbc.com" + link

                yield {'title': title, 'link': link}

        except Exception as e:
            logger.error(f"Error parsing content: {e}")
            raise ScrappingError("Failed to parse HTML content") from e
        
    def scrape(self):
        """Public method to perform scrapping and store articles."""
        logger.info(f"Starting to scraper {self.url}")
        html = self._fetch_page()
        self.articles = list(self._parse_content(html))
        logger.info(f"Successfully scrapped {len(self.articles)} articles.")
        return self.articles