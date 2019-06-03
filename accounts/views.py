from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory

from django.urls import reverse

from accounts.models import UserProfile
from accounts.forms import RegistrationForm, UserForm, ProfileForm

from robo.analytics import analises
from robo.Util import util
from category.models import Category
from articles.models import Article

from collections import OrderedDict
from operator import itemgetter    
import numpy as np


# # Create your views here.
# def signup_view(request):
#     if(request.method == 'POST'):
# #         form = UserCreationForm(request.POST)
#         form = RegistrationForm(request.POST)
#         if(form.is_valid()):
#             user = form.save()
#             # login the user
#             login(request,user)
#             return redirect('articles:list')
#     else:
# #         form = UserCreationForm()
#         form = RegistrationForm()
#     return render(request, 'accounts/signup.html', {'form':form})


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('articles:list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if(request.method =='POST'):
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            #login the user
            user = form.get_user()
            login(request,user)
            if('next' in request.POST):
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('articles:list')
    
# @login_required(login_url="/accounts/login/")    
# def view_profile(request, pk=None):
#     if pk:
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#     args = {'user': user}
#     return render(request, 'accounts/profile.html', args)

def get_relacionamento_categorias(articles, requested_categories):
    nb_noticias = float(len(articles))
    keys = [cat.slug for cat in Category.objects.all()]
    values = np.zeros(len(keys))
    related_cats = dict(zip(keys,values))
    
    for article in articles:
        temp = [category.slug for category in article.categories.all()]
        for cat in temp:
            related_cats[cat] += 1
    
    # ordenando
    related_cats = OrderedDict(sorted(related_cats.items(), key = itemgetter(1), reverse = True))
    
    for key, value in related_cats.items():
        valor = ((value/nb_noticias) * 100)
        str_valor = "%.2f" % valor
        related_cats[key] = str_valor
      
    # removendo do dict a categoria passada nos parametros
    for cat in requested_categories:
        related_cats.pop(cat)
  
    return list(related_cats.keys()), list(related_cats.values())

@login_required(login_url="/accounts/login/")    
def view_profile(request):
    user = request.user
    categorias_usuario = [cat for cat in user.userprofile.categorias.all()]
    
    article_list = Article.objects.all()
    slugs = []
    for i in range(len(categorias_usuario)):
        article_list = article_list.filter(categories=categorias_usuario[i].id).order_by('-date')
        slugs.append(categorias_usuario[i].slug)
    labels_category_relation, data_category_relation= get_relacionamento_categorias(articles=article_list, requested_categories=slugs)
#     categorias, titulo = util.categoria_to_sigla(categorias_usuario)
#     labels_category_relation, data_category_relation = analises.get_relacionamento_categorias(categorias)    
#     mais_relacionadas = util.sigla_to_categoria(labels_category_relation)[:5]
    
    mais_relacionadas = labels_category_relation[:5]
    
    
    all_categorias = Category.objects.all()
    categorias_relacionadas = [all_categorias.get(slug=item) for item in mais_relacionadas]
    
#     print('categorias_relacionadas')
#     print(categorias_relacionadas)
    
    args = {'user': user, 'categorias_relacionadas': categorias_relacionadas}
    return render(request, 'accounts/profile.html', args)
    
@login_required(login_url="/accounts/login/")
def edit_profile(request):
    user = request.user
    InlineFormSet = inlineformset_factory(User, UserProfile, fields=('categorias',), can_delete=False)
        
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        formset = InlineFormSet(request.POST, instance=user)
        if user_form.is_valid() and formset.is_valid():
            user_form.save()
            formset.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        user_form = UserForm(instance=request.user)
        formset = InlineFormSet(instance=user)
    return render(request, 'accounts/edit_profile.html', {'form': user_form, 'profile_form': formset})

