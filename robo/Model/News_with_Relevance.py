
class News_with_Relevance(object):

    def __init__(self, abstract, news, date, link, title, media, chave_relevancia_site):
        self.title = title
        self.abstract = abstract
        self.news = news
        self.date = date
        self.link = link
        self.media = media
        self.chave_relevancia_site = chave_relevancia_site
        self.categories = None

    def set_categories(self, categories):
        self.categories = categories
    