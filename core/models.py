from django.db import models

# Create your models here.

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    exercise_type = models.CharField(max_length=50)
    body_part = models.CharField(max_length=50)
    equipment = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    rating = models.FloatField()
    rating_description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

