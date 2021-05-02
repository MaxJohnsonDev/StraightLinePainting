from django.conf.urls import url
from home.views import index, contactForm

app_name = 'home'

urlpatterns = [
    url(r'^index/', 'home.views.homepage'),
    url(r'^contactForm/', 'home.views.contactForm')
]
