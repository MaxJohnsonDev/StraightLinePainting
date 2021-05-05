from django.urls import path
from reviews import views

urlpatterns = [
    path('reviews/', views.reviews_list, name='review_list')
]
