from django.shortcuts import render

from articles.models import Article
from django.http import HttpResponse
import datetime


# Create your views here.
def main(request):
    latest_articles_list = Article.objects.order_by('-pub_date')
    context = {'latest_articles_list':latest_articles_list}
    return render(request, 'main/main.html', context)