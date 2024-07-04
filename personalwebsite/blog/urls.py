from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(
        'blog/<int:pk>',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'blog/<slug:category_slug>/',
        views.CategoryPostListView.as_view(),
        name='category_posts'
    ),
    path('blog/', views.PostListView.as_view(), name='all_posts'),
]
