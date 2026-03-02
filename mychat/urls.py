from django.urls import path
from .views import user_list_view, chat_view, delete_message

urlpatterns = [
    path('users/', user_list_view, name='user_list'),
    path('chat/<str:username>/', chat_view, name='chat'),
    path('delete/<int:message_id>/', delete_message, name='delete_message'),
]