from django.contrib import admin
from .models import PreprocessedVideo, ProcessedVideo

admin.site.register(PreprocessedVideo)
admin.site.register(ProcessedVideo)