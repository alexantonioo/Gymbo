from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

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

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
