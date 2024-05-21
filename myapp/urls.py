from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.loading, name='loading'),
    path('menu/', views.menu, name='menu'),
    path('home/', views.index, name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('update-color/<int:pk>', views.update_color, name='update-color'),
]