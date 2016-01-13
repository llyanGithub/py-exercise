from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Author, articles

def index(request):
    objects = Author.objects.all()
    classification_list = {}
    for author in objects:
        if author.classification not in classification_list:
            classification_list['%s' % author.classification] = []
            continue
        classification_list[author.classification].append(author.auth_name)
    return render(request, 'index.html', {'classification_list':classification_list})

def frame(request):
    objects = articles.objects.all()

    return HttpResponse("I am frame")

def auth_frame(request, author_name): 
    author_id = Author.objects.filter(auth_name=author_name)[0].id
    obj_list = articles.objects.filter(auth_id_id = author_id)
    articles_list = []

    for article in obj_list:
        articles_list.append({'article_title': article.article_title, 'article_abstract':article.article_abstract, 'article_href':article.article_href, 'pic_href':article.pic_href})


    return render(request, 'frame.html', {'articles_list':articles_list})
