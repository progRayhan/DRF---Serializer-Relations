from django.urls import path
from app_1.api.views import SongList, SingerList, SingerDetail, SongDetail

urlpatterns = [
    path('singer/', SingerList.as_view(), name="singer_list"),
    path('singer/<str:pk>/', SingerDetail.as_view(), name="singer_detail"),
    
    path('song/', SongList.as_view(), name="song_list"),
    path('song/<str:pk>/', SongDetail.as_view(), name="song_detail"),
]