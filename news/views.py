

from django.shortcuts import render, redirect, get_object_or_404

import requests

API_KEY = 'a0acb26c543e4061870ba840c41f6d9f'


# Create your views here.
def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    contxt = {
        "articles": articles,
    }

    return render(request, 'news/index.html', contxt)


def news(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'news/home.html', context)


def category(request):

    # url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    # response = requests.get(url)
    # data = response.json()
    # articles = data['articles']

    # context = {
    #     "articles": articles,
    # }
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'news/category.html', context)
