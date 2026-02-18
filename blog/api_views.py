from rest_framework import generics
from .models import Blogs
from .serializers import BlogSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Blogs.objects.select_related('author').prefetch_related('tags').order_by('-date')
    serializer_class = BlogSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
