from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('team/', views.team, name='team'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
