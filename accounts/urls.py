from django.conf.urls import patterns, url
from accounts import views

urlpatterns = [
    url(r'^login$', views.persona_login, name='persona_login'),
]