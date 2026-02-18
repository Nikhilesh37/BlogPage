from rest_framework import serializers
from .models import Blogs, author, tag, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = ['id', 'first_name', 'Second_name', 'email']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = ['id', 'caption']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'user_email', 'text', 'post']

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blogs
        fields = ['id', 'title', 'excerpt', 'image', 'date', 'content', 'author', 'tags', 'slug', 'comments']
