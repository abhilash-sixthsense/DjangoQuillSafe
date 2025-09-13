from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("new/", views.article_create, name="article_create"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
]
