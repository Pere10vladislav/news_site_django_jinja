from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Article


def index(request, page = 1):
    articles_list = Article.objects.order_by('-pub_date')
    actual_articl = Article.objects.filter(articl_actual = True).order_by('-pub_date')[0]

    paginator = Paginator(articles_list, 10)
    page_obj = paginator.get_page(page)
    page_list = []
    date_title = 0
    for item in page_obj:
        if date_title != item.pub_date.strftime("%d %m %y"):
            date_title = item.pub_date.strftime("%d %m %y")
            page_list.append(date_title)
        page_list.append(item)
        

    context = {'articles_list':page_obj , 'actual_articl':actual_articl, 'page_list':page_list}
    return render(request, 'articles/list.html', context)

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404('Статья не найдена!')
    
    context = {'article': a}
    return render(request, 'articles/detail.html', context)