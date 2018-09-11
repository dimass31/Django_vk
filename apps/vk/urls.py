from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^group/(?P<id>[-_\d]+)/$', views.group, name='group'),
]