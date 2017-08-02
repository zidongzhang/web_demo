from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tag_search.*$', views.tag_search, name="tag_search"),
    url(r'^func_trans.*$', views.func_trans, name="func_trans"),
    url(r'^$', views.index, name="index"),
]

