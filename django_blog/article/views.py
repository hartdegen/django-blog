from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse('here will be articles')
    words = ['one', 'two', 'free', 'for']
    return render(
        request,
        'article_index.html',
        context={'words': words},
    )
