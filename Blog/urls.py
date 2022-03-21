from django.urls import path
from .views import BlogListView, BlogCreateView, BlogUpdateView, LikesCreateView


app_name = 'Blog'

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='Blog_list'),
    path('create/', BlogCreateView.as_view(), name='Blog_create'),
    path('update/<pk>/', BlogUpdateView.as_view(), name='Blog_update'),
    path('create/', LikesCreateView.as_view(), name='likecreate'),
]