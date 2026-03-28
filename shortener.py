import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "https://short.url/"

    def shorten_url(self, original_url):
        hashed_url = hashlib.md5(original_url.encode()).hexdigest()[:7]
        short_url = self.base_url + hashed_url
        self.url_mapping[short_url] = original_url
        return short_url