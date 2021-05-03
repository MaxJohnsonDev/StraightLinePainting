from django.urls import path
from home.views import index, contactForm

app_name = 'home'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path(r'^contactForm/', 'home.views.contactForm')
]
