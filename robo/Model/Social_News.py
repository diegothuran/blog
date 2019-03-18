
class Social_News(object):

    def __init__(self, abstract, news, date, link, title, media, fb_comment, fb_share, fb_reaction, fb_total):
        self.title = title
        self.abstract = abstract
        self.news = news
        self.date = date
        self.link = link
        self.media = media
        self.categories = None
        # --- Social info ---
        # Facebook info
        self.fb_comment = fb_comment
        self.fb_share = fb_share
        self.fb_reaction = fb_reaction
        self.fb_total = fb_total
        

    def set_categories(self, categories):
        self.categories = categories
