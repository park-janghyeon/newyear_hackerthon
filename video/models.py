from django.db import models
from django.utils import timezone

class Video(models.Model):
    video_id = models.CharField(max_length=100, unique=True)  # YouTube Video ID
    title = models.CharField(max_length=100)  # Title of the video
    channel_title = models.CharField(max_length=100)  # Title of the channel
    published_at = models.DateTimeField(default=timezone.now)  # Publication date and time
    view_count = models.PositiveBigIntegerField(default=0)  # View count of the video
    paid_product_placement = models.BooleanField(default=False)  # If the video has paid product placement

    def __str__(self):
        return self.title
