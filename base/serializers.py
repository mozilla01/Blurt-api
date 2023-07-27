from rest_framework import serializers
from .models import Post, Like, Reply


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField("get_likes")
    image = serializers.ImageField(required=False)

    def get_likes(self, post):
        return Like.objects.filter(post=post.id).count()

    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"
