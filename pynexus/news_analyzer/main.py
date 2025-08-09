import json
from app.scrapper import NewsScrapper
from app.analyzer import HeadlineAnalyzer
from app.exceptions import ScrappingError
from app.utils import logger

def main():
    """Main function to orchestrate the application."""

    try:
        with open('config.json', 'r') as f:
            config = json.load(f)

        scrapper = NewsScrapper(url=config['url'])
        articles = scrapper.scrape()

        if not articles:
            logger.warning("No articles were scraped. Exiting.")
            return
    
        analyzer = HeadlineAnalyzer(articles=articles)
        analyzer.save_to_csv(config["output_csv_file"])
        logger.info(f"Headlines saved to {config["output_csv_file"]}")

        analyzer.generate_word_frequency_report(config["output_report_file"])
        logger.info(f"Word frequency report saved to {config["output_report_file"]}")

        logger.info("Process completed successfully.")
    
    except FileNotFoundError:
        logger.error("Configuration file 'config.json' not found. Please create it.")

    except ScrappingError as e:
        logger.error(f"A scraping error occurred: {e}")
    
    except Exception as e:
        logger.critical(f"An unexpected critical error occurred: {e}")

if __name__ == "__main__":
    main()
