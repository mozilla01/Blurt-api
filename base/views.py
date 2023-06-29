from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
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
