# WebRAGCache
Web search RAG cache (46prp)

## Usage

To use the `crawler.py` script, follow these steps:

1. Set the required environment variables:
   - `OPENAI_API_BASE`: The base URL for the OpenAI API.
   - `OPENAI_API_KEY`: The API key for the OpenAI API.
   - `SEARCH_BASE_URL`: The base URL for the Google search API.
   - `SEARCH_API_KEY`: The API key for the Google search API.
   - `SEARCH_RESULTS_LIMIT`: The limit for the number of search results (optional, default is 7).
   - `OPENAI_MODEL`: The model to use for the OpenAI API (e.g., "gpt-4o-latest").
   - `OUTPUT_FORMAT`: The output format for the scraped content (optional, default is "markdown").
   - `NO_FALLBACK`: Whether to use fallback extraction methods (optional, default is "True").

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a Python script to use the `Crawler` class:
   ```python
   from crawler.crawler import Crawler

   # Initialize the Crawler class
   crawler = Crawler()

   # Generate search keywords and tags based on user prompt
   prompt = "Enter your search prompt here"
   result = crawler.search_and_crawl(prompt)

   # Print the result
   print(result)
   ```

4. Run the script:
   ```bash
   python your_script.py
   ```
