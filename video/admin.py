from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'title', 'channel_title', 'published_at', 'view_count', 'paid_product_placement')
    search_fields = ('title', 'channel_title')
    list_filter = ('published_at', 'paid_product_placement')
    ordering = ('-published_at',)

admin.site.register(Video, VideoAdmin)
