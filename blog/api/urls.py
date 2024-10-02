from django.urls import path
from blog.api.views import PostListAV, PostDetailAV

urlpatterns = [
    path("blog/", PostListAV.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailAV.as_view(), name="post_detail"),
]
