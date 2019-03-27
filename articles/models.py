from django.db import models
from django.template.defaultfilters import title
from docutils.parsers.rst.directives import body
from django.contrib.auth.models import User
from category.models import Category
# from django import models

# from category.models import Category
# categorias = Category.objects.all()
# categorias[0].article_set.all()
# cat = categorias[0]
# cat.parent

# from articles.models import Article
# articles = Article.objects.all()
# artigo = articles[4]
# nomes = [category.title for category in artigo.categories.all()]

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(blank=True)
    body = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    date = models.DateTimeField()
    thumb = models.TextField(blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    link = models.CharField(max_length=250, blank=True)
    
    # Gambiarra: usar o parent de categories nao como pai, mas como filho para facilitar as operacoes
    categories = models.ManyToManyField('category.Category', help_text='Categorize this item.')
    # add more fields later
    
    # commands:
    # python3 manage.py startapp categories
    # python3 manage.py makemigrations
    # python3 manage.py migrate
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:200] + '...'
    