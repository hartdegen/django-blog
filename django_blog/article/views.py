from django.views import View
from django.shortcuts import render

class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        articles = [
            {
                'id': 1,
                'name': 'Article 1',
                'description': 'Description 1'
            },
            {
                'id': 2,
                'name': 'Article 2',
                'description': 'Description 2'
            },
            {
                'id': 3,
                'name': 'Article 3',
                'description': 'Description 3'
            },
        ]
        
        context = {
            'articles': articles,
            'title': 'List of articles'
        }
        return render(request, 'article_index.html', context)