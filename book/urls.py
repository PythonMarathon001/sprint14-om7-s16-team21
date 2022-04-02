from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/
    # path('page', views.pege2, name='page2'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('allbooks', views.allbooks, name='allbooks'),
    path('allbooks/<int:pk>/', views.ID_BookView.as_view(), name='id_book'),
    path('allbooks/filters/', views.filtered_books, name='filtered_books'),
    path('allbooks/order_by_count_asc/', views.ordered_books_count_ascending, name='ordered_books_count_ascending'),
    path('allbooks/order_by_count_dsc/', views.ordered_books_count_descending, name='ordered_books_count_descending'),
    path('allbooks/order_by_name_asc/', views.ordered_books_name_ascending, name='ordered_books_name_ascending'),
    path('allbooks/order_by_name_dsc/', views.ordered_books_name_descending, name='ordered_books_name_descending'),

    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]