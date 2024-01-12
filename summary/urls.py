from django.urls import path
from .views import get_youtube_transcript_as_paragraph

urlpatterns = [
    # Define your URL patterns here
    path('transcript/<str:video_id>/', get_youtube_transcript_as_paragraph, name='youtube-transcript'),
]
