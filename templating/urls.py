from django.urls import path

from .views import hello_templates, hello_render

urlpatterns = [

    # /templates/hello/
    path('hello/', hello_templates),
    path('hello-render/', hello_render),
]
