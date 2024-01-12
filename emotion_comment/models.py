from django.db import models

#테스트용 api
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Emotion(models.Model):
    message = models.CharField(max_length=100, default='안녕하세요')
    def __str__(self):
        return self.message