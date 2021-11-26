from django.http import HttpResponse
from django.shortcuts import render


def hello(request, article_id):
    return render(request, 'index.html', context={'name': article_id})
