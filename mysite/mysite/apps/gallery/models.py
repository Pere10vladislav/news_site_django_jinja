from django.db import models

class Image(models.Model):
    title = models.CharField('Название', max_length  = 200)
    image = models.FileField(upload_to='images')
    

    def __str__(self):
        return self.title

    class Meta :
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'