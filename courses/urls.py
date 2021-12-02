from django.urls import path
from .views import (
    CategoryListView,
    CourseListView,
    LessonListView,
    PostListView,
    LikeListView,
    CommentListView,
    PostViewListView,

    CategoryDetailView,
    CourseDetailView,
    LessonDetailView,
    PostDetailView,
    LikeDetailView,
    CommentDetailView,
    PostViewDetailView,
)


urlpatterns = [
    
    path("category/", CategoryListView.as_view()),
    path("category/<int:pk>", CategoryDetailView.as_view()),

    path("course/", CourseListView.as_view()),
    path("course/<int:pk>", CourseDetailView.as_view()),

    path("lesson/", LessonListView.as_view()),
    path("lesson/<int:pk>", LessonDetailView.as_view()),

    path("post/", PostListView.as_view()),
    path("post/<int:pk>", PostDetailView.as_view()),

    path("like/", LikeListView.as_view()),
    path("like/<int:pk>", LikeDetailView.as_view()),

    path("comment/", CommentListView.as_view()),
    path("comment/<int:pk>", CommentDetailView.as_view()),

    path("postview/", PostViewListView.as_view()),
    path("postview/<int:pk>", PostViewDetailView.as_view()),
]
