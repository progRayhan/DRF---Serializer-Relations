from secrets import choice
from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
)

class Singer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    
    def __str__(self):
        return self.name
    

class Song(models.Model):
    title = models.CharField(max_length=255)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='sung_by')
    instrument = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title