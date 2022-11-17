from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.link, name="entry"),
    path("search/", views.search, name="search"),
    path("new_page/", views.New_Page, name="new"),
    path("create_page/", views.Create_new_page, name="create"),
    path("edit/", views.Show_edit_page, name="Show_edit"),
    path("random/", views.Random_Page, name="random"),
    path("page_edit/", views.edit, name="editing"),
    
     
]
