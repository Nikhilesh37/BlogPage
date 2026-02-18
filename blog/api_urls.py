from django.urls import path
from .api_views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='api-post-list'),
    path('posts/<slug:slug>/', PostDetailAPIView.as_view(), name='api-post-detail'),
]
