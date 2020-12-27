from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    )

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
#http://127.0.0.1:8000/post/2/