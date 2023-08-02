from rest_framework import serializers
from .models import Post, Like, Reply


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField("get_likes")
    comments = serializers.SerializerMethodField("no_of_comments")
    image = serializers.ImageField(required=False)

    def get_likes(self, post):
        return Like.objects.filter(post=post.id).count()

    def no_of_comments(self, post):
        return Reply.objects.filter(post=post.id).count()

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
