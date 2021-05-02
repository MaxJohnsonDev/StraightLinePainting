from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path(r'^/', views.homepage, name="homepage"),
    path(r'^contactForm/', views.contactForm, name="contactForm")
]
