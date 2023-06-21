from django.db import models
from datetime import datetime, timedelta


class Article(models.Model):
    articl_title = models.CharField('Название статьи', max_length  = 200)
    articl_text = models.TextField('Текст статьи')
    articl_crucial = models.BooleanField('Ключевая', default = False)
    articl_actual = models.BooleanField('Список актуальных', default = False)
    articl_image = models.FileField('Фотография', blank=True, upload_to='images')
    date_modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField('Дата публикации') 

    def was_changed_recently(self):
        if self.date_modified-self.pub_date >= timedelta(minutes=10):
            res = True
        else:
            res = False
        return res

    def __str__(self):
        return self.articl_title

    class Meta :
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'