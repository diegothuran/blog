from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    # ---------------------------API Documentation ---------------------------

    path('',  schema_view.with_ui('swagger', cache_timeout=0)),
    # ---------------------------Article---------------------------
    path('article/', views.ArticleListCreate.as_view()),
    path('article/<int:id>/', views.ArticleUpdateRetrievDestroy.as_view()),
    # ---------------------------Category---------------------------
    path('category/', views.CategoryListCreate.as_view()),
    path('category/<int:id>/', views.CategoryUpdateRetriveDestroy.as_view()),
    # ---------------------------Tag---------------------------
    path('tag/', views.TagListCreate.as_view()),
    path('tag/<int:id>/', views.TagUpdateRetriveDestroy.as_view()),

]
