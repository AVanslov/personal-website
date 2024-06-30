from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.PostListView.as_view(), name='all_posts'),
]
