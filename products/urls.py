from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'), # create path by product id
    path('<int:product_id>upvote', views.upvote, name='upvote'), 
]