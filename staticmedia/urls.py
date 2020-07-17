from django.urls import path
from .views import render_static, manage_media

urlpatterns = [
    # static-demo
    path('demo/', render_static),
    path('media/', manage_media)
]
