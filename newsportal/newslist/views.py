from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'newslist/home.html', context)


def about(request):
    return render(request, 'newslist/about.html', {'title': 'О портале новостей'})


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной статье
    model = Post
    # Используем другой шаблон — news.html
    template_name = 'newslist/news.html'
    # Название объекта, в котором будет выбранная пользователем статья
    context_object_name = 'news'
