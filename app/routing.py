from django.urls import path
from .consumers import *

ws_urlpatterns = [
    path('connect/', MyCons.as_asgi())
]