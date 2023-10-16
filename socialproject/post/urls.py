from django.urls import path
from post import views

urlpatterns = [
    path("create_post/", views.create_post, name="create_post"),
    path("feed/", views.feed, name="feed"),
    path('like/', views.like_post, name="like"),
]
