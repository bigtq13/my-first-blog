from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^index.html$',views.homepage, name='homepage'),
    url(r'^projects/eipT.html$',views.eipT, name='eipT'),
    url(r'^projects/chtgstoreT.html$',views.chtgstoreT, name='chtgstoreT'),
    url(r'^projects/chtselfserviceT.html$',views.chtselfserviceT, name='chtselfserviceT'),
    url(r'^projects/amrtT.html$',views.amrtT, name='amrtT'),
]
