from django.urls import path

from .views import (
    BookListView, 
    # BookDetailView, 
    BookCreateView, 
    BookUpdateView, 
    BookDeleteView, 
    BookQueryView,
    # BookDetail_CommentView,
    BookDetail_CommentListCreateView,
    HorrorBookListView,
    RomanceBookListView,
    AdventureBookListView
)


app_name = "books"
urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    # path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    path("<int:pk>/", BookDetail_CommentListCreateView, name="book-detail"),
    # path("backend/<int:pk>/", BookDetail_CommentView, name="book-detail-backend"),
    path("create/", BookCreateView.as_view(), name="book-create"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
    path("query/", BookQueryView, name="book-query"),
    path("horror/", HorrorBookListView.as_view(), name="book-horror-list"),
    path("romance/", RomanceBookListView.as_view(), name="book-romance-list"),
    path("adventure/", AdventureBookListView.as_view(), name="book-adventure-list"),
]