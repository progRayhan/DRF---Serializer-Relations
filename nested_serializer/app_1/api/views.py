from rest_framework.views import APIView
from rest_framework.response import Response
from app_1.models import Song, Singer
from app_1.api.serializers import SongSerializer, SingerSerializer

class SongList(APIView):
    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)
    
class SongDetail(APIView):
    def get(self, request, pk):
        song = Song.obejcts.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    
    
class SingerList(APIView):
    def get(self, request):
        singer = Singer.objects.all()
        serializer = SingerSerializer(singer, many=True)
        return Response(serializer.data)
    
class SingerDetail(APIView):
    def get(self, request, pk):
        singer = Singer.objects.get(pk=pk)
        serializer = SingerSerializer(singer)
        return Response(serializer.data)