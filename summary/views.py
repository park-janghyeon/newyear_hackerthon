import json
from django.http import HttpResponse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def get_youtube_transcript_as_paragraph(request, video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
        paragraph = ' '.join([item['text'] for item in transcript_list])

        # 직접 JSON 문자열 생성
        response_data = json.dumps({'video_id': video_id, 'transcript': paragraph}, ensure_ascii=False)
        return HttpResponse(response_data, content_type="application/json")

    except TranscriptsDisabled:
        return JsonResponse({'error': 'Transcripts are disabled for this video'}, status=400)

    except NoTranscriptFound:
        return JsonResponse({'error': 'No transcript found for this video'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
