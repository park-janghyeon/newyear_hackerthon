from django.urls import path
from .views import *

urlpatterns = [
    # Define your URL patterns here
    path('a', ItemList.as_view(), name='item-list'),
    path('b', EmotionView.as_view(), name='emotion-list'),
]
