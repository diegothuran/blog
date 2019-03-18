from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
        
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(RegistrationForm).save(commit=False)
        
        # Assumes .cleaned_data exists because this method is always invoked after .is_valid(), otherwise will raise AttributeError
#         cd = self.cleaned_data 
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if(commit):
            user.save()
        return user
         
        