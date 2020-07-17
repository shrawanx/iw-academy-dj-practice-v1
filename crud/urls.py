from django.urls import path
from .views import (list_all_user, detail_view_of_users,
                    create_user_info, update_user_info, delete_user_info)

app_name = 'crud'

urlpatterns = [
    # crud/list/
    # {%url 'crud:list'}
    path('list/', list_all_user, name='list'),
    path('create/', create_user_info, name='create'),
    path('detail/<int:user_id>/', detail_view_of_users, name='detail'),
    path('update/<int:user_id>/', update_user_info),
    path('delete/<int:user_id>/', delete_user_info),
]
