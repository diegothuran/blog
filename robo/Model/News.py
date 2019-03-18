
class News(object):

    def __init__(self, abstract, news, date, link, title, media):
        self.title = title
        self.abstract = abstract
        self.news = news
        self.date = date
        self.link = link
        self.media = media
        self.categories = None

    def set_categories(self, categories):
        self.categories = categories