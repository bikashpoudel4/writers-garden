import re
from math import ceil


class ArticleReadTimeEngine:
    @staticmethod
    def word_count(text):
        # Use the re (regular expression) module to find all words in the input text
        words = re.findall(r"\w+", text)
        # Return the count of words in the text
        return len(words)

    @staticmethod
    def estimate_reading_time(
        article, words_per_minute=250, seconds_per_image=10, seconds_per_tag=2
    ):
        # Calculate word count for the body, title, and description of the article
        word_count_body = ArticleReadTimeEngine.word_count(article.body)
        word_count_title = ArticleReadTimeEngine.word_count(article.title)
        word_count_description = ArticleReadTimeEngine.word_count(article.description)

        # Calculate the total word count
        total_word_count = word_count_body + word_count_title + word_count_description

        # Calculate reading time in minutes based on words per minute
        reading_time = total_word_count / words_per_minute

        # If there's a banner image, add the corresponding time in minutes
        if article.banner_image:
            reading_time += seconds_per_image / 60

        # Calculate additional reading time based on the number of tags
        tag_count = article.tags.count()
        reading_time += (tag_count * seconds_per_tag) / 60

        # Round up the reading time to the nearest minute
        reading_time = ceil(reading_time)

        # Return the estimated reading time in minutes
        return reading_time
