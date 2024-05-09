from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.loading, name='loading'),
    path('home/', views.index, name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('change_pixel/<int:pk>/', views.change_rgb, name="change_pixel"),
]