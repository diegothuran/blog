from django.shortcuts import render
from rest_framework import generics, filters, permissions
from articles import models
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from category.models import Category, Tag
from . import pagination


# ---------------------------Article---------------------------

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    permission_classes = []

    search_fields = ('abstract',)
    filter_fields = '__all__'
    pagination_class = pagination.CustomPagination

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return serializers.ArticleSerializer
        return serializers.ArticleCreateSerializer


class ArticleUpdateRetrievDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    lookup_field = 'id'
    permission_classes = []

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return serializers.ArticleSerializer
        return serializers.ArticleCreateSerializer


# --------------------------- Category ---------------------------

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    permission_classes = []
    serializer_class = serializers.CategorySerializer
    filter_fields = '__all__'
    pagination_class = pagination.CustomPagination


class CategoryUpdateRetriveDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'id'
    permission_classes = []
    serializer_class = serializers.CategorySerializer

# --------------------------- Tag ---------------------------

class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    permission_classes = []
    serializer_class = serializers.TagSerializer
    filter_fields = '__all__'
    pagination_class = pagination.CustomPagination


class TagUpdateRetriveDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    lookup_field = 'id'
    permission_classes = []
    serializer_class = serializers.TagSerializer
