from django.urls import path

from .views import add_two_numbers, add_two_numbers_in_rest, info_view

from .class_views import InfoClassBasedViews

urlpatterns = [
    # rest/add/
    path('add/', add_two_numbers),
    path('v2/add/', add_two_numbers_in_rest),
    path('info/', info_view),
    path('info/<int:pk>/', info_view),

    # rest/info/class-based/
    path('info/class-based/', InfoClassBasedViews.as_view())
]
