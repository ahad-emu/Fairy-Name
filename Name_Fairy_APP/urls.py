from django.urls import path
from Name_Fairy_APP import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
]
