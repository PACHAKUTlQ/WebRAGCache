import os
import requests
from urllib.parse import quote, unquote


class GoogleSearch:

    def __init__(self):
        self.search_base_url = os.getenv("SEARCH_BASE_URL")
        self.search_api_key = os.getenv("SEARCH_API_KEY")
        self.limit = os.getenv("SEARCH_RESULTS_LIMIT", 7)

    def search_google(self, search_keyword):
        # Encode search keyword if it is not already encoded
        if search_keyword == unquote(search_keyword):
            search_keyword = quote(search_keyword)
        url = f"{self.search_base_url}/google/search?text={search_keyword}&limit={self.limit}"
        headers = {"Authorization": f"Bearer {self.search_api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
