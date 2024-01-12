# summary/models.py

from django.db import models
from video.models import Video

class PreprocessedVideo(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)  # Video 모델을 외래 키로 참조
    originalText = models.TextField()

    def __str__(self):
        return self.originalText


# summary/models.py
class ProcessedVideo(models.Model):
    preprocessed_video = models.ForeignKey(PreprocessedVideo, on_delete=models.CASCADE)  # PreprocessedVideo 모델을 외래 키로 참조
    summaryText = models.TextField()

    def __str__(self):
        return self.summaryText
