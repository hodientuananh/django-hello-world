from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path('users/', views.UserViewSet.as_view(), name='users'),
    path('groups/', views.GroupViewSet, name='groups'),
]
