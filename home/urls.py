from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    pat("", views.homepage, name="homepage"),
    path("contactForm", views.contactForm, name="contactForm")
]
