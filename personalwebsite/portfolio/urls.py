from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', views.PortfolioListView.as_view(), name='all_projects'),
]
