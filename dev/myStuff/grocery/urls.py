from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration',views.Registration,name='Registration'),
    path('login',views.Login,name='Login'),
    path('add_items',views.add_items,name='add_items'),
    path('order_items',views.order_items,name='order_items')
]