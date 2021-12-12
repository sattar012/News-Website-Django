

from newsapi import NewsApiClient
from django.shortcuts import render, redirect, get_object_or_404

import requests

from django.contrib import messages

from newsapp.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

from .models import Contact

import razorpay

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

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
    keyword = request.GET.get('keyword')
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'news/home.html', context)


def category(request):
    category = request.GET.get('category')

    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'news/category.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)
    articles = data['articles']

    context = {
        'articles': articles,
    }

    return render(request, 'news/search.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if len(name) < 2 or len(email) < 3 or len(subject) < 5 or len(message) < 5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              subject=subject, message=message)
            contact.save()
            messages.success(
                request, 'Your issue is recorded.Thanks!! hope you wait till one of our executive reach you')
    return render(request, 'news/contact.html')


def about(request):
    return render(request, 'news/about.html')


def donate(request):

    DATA = {
        "amount": 50000,
        "currency": "INR",
        "payment_capture": 1,
    }
    payment_order = client.order.create(data=DATA)
    payment_order_id = payment_order['id']

    context = {
        'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }

    return render(request, 'news/donate.html', context)


# def sattar(request):
#     newsapi = NewsApiClient(api_key=API_KEY)
#     news_sources = newsapi.get_sources()

#     top_headlines = newsapi.get_top_headlines(
#         q='World War',
#         language='en',
#     )
#     for article in top_headlines['articles']:
#         print('Title : ', article['title'])
#         print('Description : ', article['description'], '\n\n')
#     return render(request, 'news/search1.html')
