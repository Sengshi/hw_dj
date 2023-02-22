# coding=utf-8
from datetime import datetime

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author

    def get_date(self):
        date = self.pub_date
        return date.strftime('%Y-%m-%d')
