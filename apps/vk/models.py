# -*- coding: utf-8 -*-

from django.db import models


class Group(models.Model):
    name = models.CharField(u'Название группу', max_length=255)
    link = models.CharField(u'Ссылка на группу', max_length=1024)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"


class Post(models.Model):
	group = models.ForeignKey(Group, verbose_name=u'Группа', related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
	text = models.TextField(u'Текст поста')
	link = models.CharField(u'Ссылка на пост', max_length=1024)
	comment_count = models.PositiveIntegerField(u'Количество комментариев', default=0)
	views_count = models.PositiveIntegerField(u'Количество просмотров', default=0)
	likes_count = models.PositiveIntegerField(u'Количество лайков', default=0)
	repost_count = models.PositiveIntegerField(u'Количество репостов', default=0)

	def __str__(self):
		return self.link

	class Meta:
		verbose_name=u'Пост'
		verbose_name_plural=u'Посты'

class Freinds(models.Model):
	pass
