from django.urls import path

from . import views

urlpatterns = [
    # everything here will be account/ .... 
    # eg first path will be account/register
    path('register', views.register, name="Register page"),
    path('login', views.login, name="Login page"),
    path('<int:id>/', views.update_user, name="edit_page"),
    path('logout',views.logout, name="logout")
]