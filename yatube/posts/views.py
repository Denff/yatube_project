# from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница со списком постов
def group_posts(request):
  return HttpResponse('Список постов по группам')

# Страница с информацией об конкретной группе постов
def group_posts_detail(request, slug):
    return HttpResponse(f'Группа {slug}') 