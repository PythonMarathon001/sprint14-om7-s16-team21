from django.urls import path
from . import views
app_name='user'
urlpatterns=[
    path('all_users/',views.all_users,name='all_users'),
    path('add_user/',views.add_user,name='add_user'),
    path('add_user/<int:id>',views.add_user,name='update_user')
]