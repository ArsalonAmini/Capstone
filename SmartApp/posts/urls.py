from django.conf.urls import url
from .views import (
    posts_create,
    posts_list,
    posts_detail,
    posts_update,
    posts_delete,
)
urlpatterns = [
    url(r'^$', posts_list),
    url(r'^create/$', posts_create),
    url(r'^(?P<id>\d+)/$', posts_detail, name='detail'),
    url(r'^update/$', posts_update),
    url(r'^delete/$', posts_delete),
]

