from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('author/<int:pk>/update/', views.update_author, name='update_author'),
    path('book/<int:pk>/update/', views.update_book, name='update_book'),
    path('author/<int:pk>/delete/', views.delete_author, name='delete_author'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book')
]
