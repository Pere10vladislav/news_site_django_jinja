# Generated by Django 4.2.1 on 2023-06-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_articl_image_alter_article_articl_crucial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articl_actual',
            field=models.BooleanField(default=False, verbose_name='Список актуальных'),
        ),
        migrations.AlterField(
            model_name='article',
            name='articl_image',
            field=models.FileField(blank=True, upload_to='images', verbose_name='Фотография'),
        ),
    ]
