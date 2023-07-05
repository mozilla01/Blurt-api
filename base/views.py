from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Like, Reply
from .serializers import PostSerializer, LikeSerializer, ReplySerializer
from django.db.models import Q


@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "List of posts": "posts/",
        "Specific post": "post/<id>/",
        "Create post": "create-post/",
    }
    return Response(api_urls)


@api_view(["GET"])
def posts(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    posts = Post.objects.filter(Q(user__icontains=q)).order_by("-created")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def post_detail(request, id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def edit_post(request, id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=400)


@api_view(["DELETE"])
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return Response("Post deleted")


@api_view(["GET"])
def get_likes(request, user):
    likes = Like.objects.filter(user=user)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_like(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Object created")


@api_view(["POST"])
def like_post(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        print("valid")
        user = serializer.data.get("user")
        id = serializer.data.get("post")[0]
        like = Like.objects.get(user=user)
        post = Post.objects.get(id=id)
        if like.post.contains(post):
            like.post.remove(post)
        else:
            like.post.add(post)
        like.save()
        return Response("Feedback recorded")
    else:
        print(serializer.errors)
        return Response("Something went wrong")


@api_view(["GET"])
def get_replies(request, id):
    replies = Reply.objects.filter(post=id).order_by("-created")
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def send_reply(request):
    serializer = ReplySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return Response("Something went wrong...")
