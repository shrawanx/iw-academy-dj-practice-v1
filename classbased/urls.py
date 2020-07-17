from django.urls import path

app_name = 'classbased'

from .views import FirstView, FirstTemplate, FirstTemplateRedirect

from .crud_views import Create, List, Detail, Update, Delete

urlpatterns = [
    path('first/', FirstView.as_view()),
    path('template/', FirstTemplate.as_view()),
    path('template1/', FirstTemplateRedirect.as_view()),
    path('template2/', FirstTemplateRedirect.as_view()),
    path('template3/', FirstTemplateRedirect.as_view()),

    path('create/', Create.as_view(), name='create'),
    path('list/', List.as_view(), name='list'),
    path('detail/<int:id>/', Detail.as_view(), name='detail'),
    path('update/<int:id>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
