from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView
urlpatterns = [
    path('',BlogListView.as_view(),name='home'),
    path('blog/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('blog/new/',BlogCreateView.as_view(),name='post_new'),
    path('blog/<int:pk>/edit',BlogUpdateView.as_view(),name='post_update'),
]

