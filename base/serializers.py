from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField("get_likes")
    comments = serializers.SerializerMethodField("no_of_comments")
    image = serializers.ImageField(required=False)

    def get_likes(self, post):
        return Like.objects.filter(post=post.id).count()

    def no_of_comments(self, post):
        return Post.objects.filter(parent=post.id).count()

    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
