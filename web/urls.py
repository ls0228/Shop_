from django.urls import path
from . import views
from .views import item_list, orders

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('team/', views.team, name='team'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('item_list/', item_list, name='item_list'),
    path('orders/', orders, name='orders')
]
