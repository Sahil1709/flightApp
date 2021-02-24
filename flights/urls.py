from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirm-booking/<int:id>', views.book , name='confirm-booking'),
    path('test', views.test, name="Users page")
]