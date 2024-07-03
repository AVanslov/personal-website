from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path(
        'portfolio/<int:pk>',
        views.PortfolioDetailView.as_view(),
        name='project_detail'
    ),
    path(
        'portfolio/<slug:category_slug>/',
        views.CategoryProjectListView.as_view(),
        name='category_projects'
    ),
    path(
        'portfolio/',
        views.PortfolioListView.as_view(),
        name='all_projects'
    ),
]
