from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
<<<<<<< Updated upstream
=======
from django.utils import timezone
>>>>>>> Stashed changes

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        Group,
        related_name='core_user_set',
        related_query_name='core_user',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_user_set',
        related_query_name='core_user',
        blank=True
    )
    
    class Meta:
        db_table = 'core_user'

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.SET_NULL, null=True, blank=True)
    exercises = models.ManyToManyField('Exercise')
    age = models.IntegerField(null=True, blank=True)
    weight = models.JSONField(default=list)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    reviews = models.JSONField(default=list)

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    exercise_type = models.CharField(max_length=50)
    body_part = models.CharField(max_length=50)
    equipment = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    rating = models.FloatField()
    rating_description = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    is_done = models.BooleanField(default=False)
