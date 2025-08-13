from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['post', 'author_username','content','create_at','update_at']
