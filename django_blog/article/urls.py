from django.urls import path
from django_blog.article.views import ArticleIndexView

urlpatterns = [
    path('', ArticleIndexView.as_view(), name='article_index'),
]
