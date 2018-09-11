from django.conf.urls import url

from django.utils.translation import ugettext_lazy as _

from .views import *
import django.contrib.auth.views


urlpatterns = [
	url(r'^logout/$', django.contrib.auth.views.logout_then_login, name='logout'),
]
