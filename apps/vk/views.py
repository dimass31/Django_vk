# -*- coding: utf-8 -*-
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import posts

from .models import Group, Post


def main(request):
	context = {}
	if request.user.is_authenticated:
		group = request.GET.get("group")
		#freinds = requests.GET.get()
		if group:
			new_group, created = Group.objects.get_or_create(name=group, link="https://vk.com/" + str(group))
			r = requests.get("https://api.vk.com/method/wall.get?domain=" + str(group) + "&access_token=" + request.user.token + "&count=100&v=5.74")
			posts.delay(group, r.json()['response']['items'])
	context['groups'] = Group.objects.all()
	return render(request, 'main.html', context)


def group(request, id):
	context = {}
	context['group'] = Group.objects.get(id=id)
	return render(request, 'group.html', context)