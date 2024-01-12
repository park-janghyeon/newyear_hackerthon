from rest_framework import serializers
from .models import PreprocessedVideo, ProcessedVideo

class PreprocessedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreprocessedVideo
        fields = '__all__'

class ProcessedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedVideo
        fields = '__all__'