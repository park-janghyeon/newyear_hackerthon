#테스트용
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, Emotion
from .serializers import ItemSerializer

class ItemList(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Emotion
from .serializers import EmotionSerializer

class EmotionView(APIView):
    def get(self, request, format=None):
        emotion = Emotion.objects.first()  # 첫 번째 Greeting 인스턴스를 가져옵니다.
        if not emotion:
            emotion = Emotion()  # 인스턴스가 없다면 새로 생성합니다.
            emotion.save()

        # '안녕하세요'를 '안녕'으로 변환
        emotion.message = emotion.message[:2]
        emotion.save()

        serializer = EmotionSerializer(emotion)
        return Response(serializer.data)

    #post로 문자를 넣으면 그 문자를 저장하고 다시 get으로 문자를 받아온다.
    def post(self, request, format=None):
        emotion = Emotion.objects.first()
        emotion.message = request.data.get('message')
        emotion.save()

        serializer = EmotionSerializer(emotion)
        return Response(serializer.data)