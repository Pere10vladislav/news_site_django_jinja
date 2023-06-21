from django.urls import path


from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'main'),
    path('<int:page>', views.index, name = 'main'),
    path('detail/<int:article_id>', views.detail, name = 'detail'),
]