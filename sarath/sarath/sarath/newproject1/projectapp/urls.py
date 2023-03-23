from django.urls import path
from . import views
# app_name='projectapp'
urlpatterns =[
    path("home",views.home,name="home"),
    path("movie/<int:movie_id>/",views.detail,name="detail"),
    path("add_movies",views.add_movies,name='add_movies'),
    path("update/<int:id>/",views.updatehtml,name="update"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("register",views.register_request,name="register"),
    path("login", views.login_request, name="login"),
    path("logout",views.logout_request,name="logout")
]