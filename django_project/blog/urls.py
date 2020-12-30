from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    BookListView,
    BookDetailView,
    AddCommentView
)

urlpatterns = [
    path('', BookListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('about/', views.about, name='blog-about'),
    path('fiction/', views.fiction, name='blog-fiction'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add-comment')
]