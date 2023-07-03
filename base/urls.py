from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_overview, name="overview"),
    path("posts/", views.posts, name="posts"),
    path("post/<str:id>/", views.post_detail, name="post-detail"),
    path("create-post/", views.create_post, name="create-post"),
    path("edit-post/<str:id>/", views.edit_post, name="edit-post"),
    path("delete-post/<str:id>/", views.delete_post, name="delete-post"),
    path("get-likes/<str:user>/", views.get_likes, name="get-likes"),
    path("create-like-object/", views.create_like, name="create-like-object"),
    path("like-post/", views.like_post, name="like-post"),
]
