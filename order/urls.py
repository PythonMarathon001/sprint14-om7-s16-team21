from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    # path('', views.index, name='index'),
    path('all_orders', views.all_orders, name='all_orders'),

]