from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Article

def index(request, articleNum):
    print articleNum
    articleList = Article.objects.order_by('id')
    articleContent = open('/Users/llyan/django-learn/02/mysite/blogs/static/txt/02.txt').read()
    articleDetial = Article.objects.get(id = articleNum) 
    template = loader.get_template('blogs/index.html')
    context = {
            'articleList':articleList,
            'articleContent':articleContent,
            'articleDetial':articleDetial,
    }
    return HttpResponse(template.render(context, request))
