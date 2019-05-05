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

from robo.teste import teste_db
from robo.Util import util
from category.models import Category


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

@login_required(login_url="/accounts/login/")    
def view_profile(request):
    user = request.user
    categorias_usuario = [cat for cat in user.userprofile.categorias.all()]

    categorias, titulo = util.categoria_to_sigla(categorias_usuario)
    labels_category_relation, data_category_relation = teste_db.get_relacionamento_categorias(categorias)    
    
    mais_relacionadas = util.sigla_to_categoria(labels_category_relation)[:5]
    all_categorias = Category.objects.all()
    categorias_relacionadas = [all_categorias.get(title=item) for item in mais_relacionadas]
        
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

