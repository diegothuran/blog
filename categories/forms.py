from django import forms
from category.models import Category


class MultipleChoiceForm(forms.Form):
#     CHOICES = [[x.id, x.title] for x in Category.objects.all()]
    CHOICES = [[cat.slug, cat.title] for cat in Category.objects.all()]
    picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)
    