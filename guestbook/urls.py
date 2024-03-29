from django.urls import path
from . import views

urlpatterns = [
    path('guestbook/', views.guestbook_view, name='guestbook'),
    path('chat/', views.chat_view, name='chat'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
]
