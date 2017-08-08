from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^index.html$',views.homepage, name='homepage'),
    url(r'^projects/eipT.html$',views.eipT, name='eipT'),
    url(r'^projects/chtgstoreT.html$',views.chtgstoreT, name='chtgstoreT'),
    url(r'^projects/chtselfserviceT.html$',views.chtselfserviceT, name='chtselfserviceT'),
    url(r'^projects/amrtT.html$',views.amrtT, name='amrtT'),
    url(r'^projects/post_list.html$',views.post_list, name='post_list'),
    url(r'^projects/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^projects/post/new/$', views.post_new, name='post_new'),
    url(r'^projects/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
