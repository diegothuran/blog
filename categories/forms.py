from django import forms
from category.models import Category


class MultipleChoiceForm(forms.Form):
#     CHOICES = [[x.id, x.title] for x in Category.objects.all()]
    CHOICES = [[cat.slug, cat.title] for cat in Category.objects.all()]
    categorias = forms.MultipleChoiceField(label='', choices=CHOICES, required=False, 
                        widget=forms.CheckboxSelectMultiple({'class' : 'toggle'}))
#     picked.widget.attrs.update({'class': 'special'})

#     start_date=forms.DateField(widget = forms.SelectDateWidget())
#     end_date=forms.DateField(widget = forms.SelectDateWidget())
    