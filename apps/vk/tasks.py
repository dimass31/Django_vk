import logging
 
from django.urls import reverse
from .models import Group, Post
from ..celery import app
 
 
@app.task
def posts(group_name, posts):
    group = Group.objects.get(name=group_name)
    comments = 0
    views = 0
    likes = 0
    reposts = 0
    for post in posts:
        if 'comments' in post:
            comments = post['comments']['count']
        if 'views' in post:
            views = post['views']['count']
        if 'likes' in post:
            likes = post['likes']['count']
        if 'reposts' in post:
            reposts = post['reposts']['count']
        Post.objects.get_or_create(group=group, text=post['text'], link='https://vk.com/wall' + str(post['owner_id']) + '_' + str(post['id']), comment_count=comments, views_count=views, likes_count=likes, repost_count=reposts)
