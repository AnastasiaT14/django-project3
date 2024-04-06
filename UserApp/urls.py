from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.user_list, name='user_list'),
    path('create/', views.add_user, name='add_user'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user')
]
