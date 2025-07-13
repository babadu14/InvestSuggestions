from django.urls import path
from market.views import DashboardView
urlpatterns = [
    path('<str:coin>', DashboardView.as_view(), name='dashboard')
]