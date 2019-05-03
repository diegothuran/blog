from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# from accounts.models import UserProfile
# a = UserProfile.objects.all()[0]
# nomes = [category.title for category in a.categories.all()]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField('category.Category')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)