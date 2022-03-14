from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя категории')

    def __str__(self):
        return self.name
