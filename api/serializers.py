from rest_framework import serializers
from articles import models
from django.contrib.auth.models import User
from category.models import Category, Tag


# ---------------------------User---------------------------

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'is_superuser', 'is_staff', 'is_active',
            'password', 'first_name')


# ---------------------------Article---------------------------

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = models.Article
        fields = '__all__'
        depth = 1


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = (
            'id', 'title', 'slug', 'body', 'date', 'thumb',
            'author', 'link', 'categories')


# ---------------------------Category---------------------------


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# ---------------------------Tags---------------------------

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
