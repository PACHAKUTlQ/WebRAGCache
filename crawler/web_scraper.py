import trafilatura
import os


class WebScraper:

    def __init__(self):
        self.output_format = os.getenv("OUTPUT_FORMAT", "markdown")
        self.no_fallback = os.getenv("NO_FALLBACK", "True") == "True"

    def scrape_page(self, url):
        try:
            # Fetch original html code of the page
            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                content = trafilatura.extract(downloaded,
                                              output_format=self.output_format,
                                              no_fallback=self.no_fallback)
                return content
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None