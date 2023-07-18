from django.urls import path
from .views import ( 
    CommentListView,
    # CommentDetailView,
    # CommentCreateView,
    CommentDeleteView
) 

app_name = 'comments'
urlpatterns = [
    path('', CommentListView.as_view(), name='comment-list'),
    # path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    # path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]