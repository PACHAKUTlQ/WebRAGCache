import datetime
import os
from openai import OpenAI
import json
from dotenv import load_dotenv


class KeywordGenerator:

    def __init__(self):
        # Load environment variables from .env file in root directory
        load_dotenv(
            dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

        self.api_base = os.getenv("OPENAI_API_BASE")
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL")

    def generate_keywords_and_tags(self, prompt):
        current_date = datetime.datetime.now().strftime("%Y.%m.%d")

        keyword_gen_prompt = f"""
        You are an expert in generating professional Google search keywords and tags based on user prompts.
        The prompts of users may contain unnecessary information, and may not be professional and well-formatted. Your task is to extract the key information that requires searching, and generate:
        1. A concise Google search keyword composed of important keywords separated by spaces.
        2. A list of tags related to the search (for analytics purposes).

        Note that the search results based on your keywords will be fed into Large Language Models to assist in answering the user's query. Therefore, you should generate search keywords for information you think requires searching most, instead of directly searching user prompt.

        If the user asks about time-related information (e.g. news, weather, latest progress in a certain field), one of the tags must be the current date: "{current_date}".
        The output should be a JSON text in the following format:
        {{
        "search_keyword": "example search keyword",
        "tags": ["tag1", "tag2", "tag3"]
        }}

        Only provide the JSON output, without any explanations.

        Examples:

        Example 1:
        User prompt: "text embedding"
        Output:
        {{
        "search_keyword": "text embedding",
        "tags": ["embedding", "NLP", "LLM", "RAG"]
        }}

        Example 2:
        User prompt: "What happened in New York recently?"
        Output:
        {{
        "search_keyword": "New York latest news",
        "tags": ["New York", "news", "{{current_date}}"]
        }}

        Example 3: (In this example, user prompt contains unnecessary information. Necessary information to search is Spotify's frontend tech stack instead of user developing chatbot website.)
        User prompt: "I want to develop an AI chatbot website using frontend tech stack similar to Spotify."
        Output:
        {{
        "search_keyword": "Spotify frontend tech stack",
        "tags": ["Spotify", "frontend", "tech stack"]
        }}
        """

        client = OpenAI(base_url=self.api_base, api_key=self.api_key)
        completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": keyword_gen_prompt
                },
                {
                    "role":
                    "user",
                    "content":
                    f"Now please generate json based on user prompt:```\n{prompt}\n```"
                },
            ],
        )

        keywords_and_tags = completion.choices[0].message.content.strip()

        # Remove markdown codeblock if present
        if keywords_and_tags.startswith(
                "```json\n") and keywords_and_tags.endswith("```"):
            keywords_and_tags = keywords_and_tags[8:-3].strip()

        # Parse the json and check if it is valid
        try:
            keywords_and_tags_json = json.loads(keywords_and_tags)
        except json.JSONDecodeError:
            print(
                f"Warning: The generated JSON: {keywords_and_tags} is not valid. Generating again..."
            )
            # Retry generating keywords and tags
            return self.generate_keywords_and_tags(prompt)

        return keywords_and_tags_json
