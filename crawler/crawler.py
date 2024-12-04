import asyncio
from crawler.keyword_generator import KeywordGenerator
from crawler.google_search import GoogleSearch
from crawler.web_scraper import WebScraper


class Crawler:

    def __init__(self):
        self.keyword_generator = KeywordGenerator()
        self.google_search = GoogleSearch()
        self.web_scraper = WebScraper()

    def generate_keywords_and_tags(self, prompt):
        return self.keyword_generator.generate_keywords_and_tags(prompt)

    def search_google(self, search_keyword):
        return self.google_search.search_google(search_keyword)

    async def scrape_pages(self, urls):
        tasks = [self.web_scraper.scrape_page(url) for url in urls]
        return await asyncio.gather(*tasks)

    def search_and_crawl(self, prompt):
        keywords_and_tags = self.generate_keywords_and_tags(prompt)
        search_keyword = keywords_and_tags['search_keyword']
        tags = keywords_and_tags['tags']

        search_results = self.search_google(search_keyword)
        urls = [result['url'] for result in search_results]
        loop = asyncio.get_event_loop()
        contents = loop.run_until_complete(self.scrape_pages(urls))

        for result, content in zip(search_results, contents):
            result['content'] = content

        return {
            'search_keyword': search_keyword,
            'tags': tags,
            'results': search_results
        }
