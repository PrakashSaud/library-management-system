from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.AllBooksListView.as_view(), name="all_book_list"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book_detail"),
    path('book/<int:pk>', views.BookUpdateView.as_view(), name="book_update"),
    path('book/create', views.BookAddView.as_view(), name="book_add"),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view(), name="book_delete"),


]