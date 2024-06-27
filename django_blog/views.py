from django.shortcuts import render
from django.views.generic import TemplateView

# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'The World',
#     })


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'The World'
        return context


def about(request):
    return render(request, 'about.html')
