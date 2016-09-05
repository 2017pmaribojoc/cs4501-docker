__author__ = 'Patrick'
from django.conf.urls import url

from . import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home.index, name='index'),
    url(r'^2$', home.index2, name='index2'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)