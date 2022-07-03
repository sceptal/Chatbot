from django.urls import path
from my_app.views import home_page, chat_bot_view

urlpatterns = [
    path('', home_page),
    path('home_page', home_page),
    path('chat_bot', chat_bot_view),
]
