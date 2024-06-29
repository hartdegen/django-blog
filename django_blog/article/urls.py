from django.urls import path
from django_blog.article.views import ArticleIndexView, article_show

urlpatterns = [
    path('', ArticleIndexView.as_view(), name='article_index'),
    path('<str:tags>/<int:article_id>/', article_show, name='article_show'),
]
