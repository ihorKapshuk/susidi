from django.urls import path

from . import views

urlpatterns = [
    path("main/", views.index, name="main"),
    path("announcements/", views.announcements, name="announcements"),
    path("complaints/", views.complaints, name="complaints"),
    path("lost/", views.lost, name="lost"),
    path("helpful/", views.helpful, name="helpful"),
    path("user_office/", views.user_office, name="user_office"),
    path("nums/", views.nums_control, name="nums"),
    path("add_num/", views.add_num, name="add_num"),
    path("del_num/<int:id>/", views.del_num, name="del_num"),
    path("add_anon/", views.add_anon, name="add_anon"),
    path("update_anon/<int:id>/", views.update_anon, name="update_anon"),
    path("del_anon/<int:id>/", views.del_anon, name="del_anon"),
]