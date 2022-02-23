from django.urls import path
from .views import BookApiView
app_name='api'
urlpatterns=[
    path("", BookApiView.as_view(), name="home")
]