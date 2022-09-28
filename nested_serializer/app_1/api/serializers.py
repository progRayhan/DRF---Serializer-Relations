from app_1.models import Singer, Song
from rest_framework import serializers

        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
        
class SingerSerializer(serializers.ModelSerializer):
    sung_by = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'sung_by']
        