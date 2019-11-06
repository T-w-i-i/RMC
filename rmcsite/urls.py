from django.urls import path
from .views import HomeView

app_name = 'rmcsite'

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
]
