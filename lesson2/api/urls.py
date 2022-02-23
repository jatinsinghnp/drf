from django.urls import path, include
from .views import BlogApiView, BlogDetailview

app_name = "api"
urlpatterns = [
    path("", BlogApiView.as_view(), name="blog"),
    path("blog/<int:pk>/", BlogDetailview.as_view(), name="blog-detail"),
]
