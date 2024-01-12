from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'title', 'channel_title', 'published_at', 'view_count', 'paid_product_placement']
