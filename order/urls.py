from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    # path('', views.index, name='index'),
    path('all_orders', views.all_orders, name='all_orders'),
    path('ordered_orders', views.ordered_orders, name='ordered_orders'),
    path('filtered_orders', views.filtered_orders, name='filtered_orders'),
    path('add_order',views.add_order,name='add_order'),
    path('add_order/<int:id>',views.add_order,name='update_order'),
]