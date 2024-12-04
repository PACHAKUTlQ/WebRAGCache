import json
from crawler.crawler import Crawler


def main():
    # Create an instance of Crawler
    crawler = Crawler()

    # Ask for user prompt
    prompt = input("Enter your prompt: ")

    # Generate search words and keywords, do the search, scrape the pages
    output = crawler.search_and_crawl(prompt)

    # Save the output into output.json
    with open('output.json', 'w') as output_file:
        json.dump(output, output_file, indent=4)


if __name__ == "__main__":
    main()
