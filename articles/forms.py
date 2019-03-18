from django import forms
from . import models
 
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
#         fields = ('title', 'slug', 'body', 'thumb')
        fields = ('title', 'slug', 'body', 'date', 'thumb', 'author', 'link', 'categories')
