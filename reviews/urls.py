from django.urls import path
from reviews import views

app_name = 'review'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('post', views.submitReview, name='submitReview'),
]
