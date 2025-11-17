class KeywordEngine:
    def __init__(self, pages):
        self.pages = pages

    def run(self, keyword, *args, **kwargs):
        func = getattr(self.pages, keyword, None)
        if callable(func):
            return func(*args, **kwargs)
        raise AttributeError("Keyword not found")
