# coding: utf-8
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

from django.db import models
import vk
import json


AbstractUser._meta.get_field('last_name').blank = True
AbstractUser._meta.get_field('last_name').null = True
AbstractUser._meta.get_field('first_name').blank = False
AbstractUser._meta.get_field('first_name').null = False


class User(AbstractUser):
    token = models.CharField(u'token', max_length=255, blank=True, null=True)

    def __unicode__(self):
        session = vk.Session()
        vkapi = vk.API(session, v='5.35')
        freinds = vkapi.friends.get(access_token=self.token)
        freinds = str(freinds)
        return freinds

    def freinds(self):
        session = vk.Session()
        vkapi = vk.API(session, v='5.35')
        freinds = vkapi.friends.get(access_token=self.token, fields='domain', count=5, order='random')
        #freinds = json.dumps(freinds)
        f = freinds['items']
        return f

