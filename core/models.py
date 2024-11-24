from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

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



# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

# Enum for roles
class Role(models.TextChoices):
    CLIENT = 'client', _('Client')
    TRAINER = 'trainer', _('Trainer')

# User Model
class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=Role.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return f"{self.name} ({self.username})"

# Trainer model
class Trainer(models.Model):
    #username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default="example@example.com")
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=Role.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trainer_profile')
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"Trainer: {self.user.name}"

# Client model
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')
    exercises = models.ManyToManyField(Exercise, blank=True, related_name='clients')

    def __str__(self):
        return f"Client: {self.user.name}"
    

