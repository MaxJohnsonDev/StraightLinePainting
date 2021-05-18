from django.urls import path
from reviews import views

app_name = 'reviews'

urlpatterns = [
    #path('', views.review_list, name='review_list'),
    path('', views.post_list, name='review_list'),
    path('post', views.submitReview, name='submitReview'),
    path('success', views.success, name='success'),
]
