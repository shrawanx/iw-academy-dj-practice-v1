from django.urls import path

app_name = 'statusapp'

from .views import StatusMessageCreateView, StatusMessageDeleteView

urlpatterns = [
    # /statusapp/create/
    path('create/', StatusMessageCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', StatusMessageDeleteView.as_view(), name='delete'),
]
