from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, BaseUserManager
from django.db import models

from django.utils import timezone


from django.utils.translation import gettext_lazy as _




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
    trainer = models.ForeignKey('TrainerProfile', on_delete=models.SET_NULL, null=True, blank=True)
    exercises = models.ManyToManyField('Exercise')
    age = models.IntegerField(null=True, blank=True)
    weight = models.JSONField(default=list)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    reviews = models.JSONField(default=list)

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    whatsapp_link = models.URLField(max_length=255, blank=True, null=True)
    clients = models.ManyToManyField(ClientProfile, related_name="trainers")

    #metodos de trainer
    def create_weekly_plan(self, client, plan_data):
        if client not in self.clients.all():
            raise ValueError(f"{client.name} no está asignado a este entrenador.")
        plan = WeeklyPlan.objects.create(client=client, trainer=self, **plan_data)
        return plan

    def modify_weekly_plan(self, plan, modifications):
        if plan.client not in self.clients.all():
            raise ValueError(f"Este cliente no pertenece a este entrenador.")
        if plan.is_completed():
            raise ValueError("No se pueden modificar planes ya completados.")
        for field, value in modifications.items():
            if field in ["start_date", "end_date"] and plan.is_partially_completed():
                continue
            setattr(plan, field, value)
        plan.save()
        return plan

    def delete_client(self, client):
        if client in self.clients.all():
            self.clients.remove(client)
            return f"Cliente {client.name} eliminado correctamente."
        else:
            return f"Cliente {client.name} no está asignado a este entrenador."

    def create_review(self, client, review_data):
        if client not in self.clients.all():
            raise ValueError(f"{client.name} no está asignado a este entrenador.")
        review = ClientReview.objects.create(client=client, trainer=self, **review_data)
        return review

    def __str__(self):
        return self.name
    

class WeeklyPlan(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField()

    def is_partially_completed(self):
        return False

    def is_completed(self):
        return False


class ClientReview(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f"Revisión de {self.client.name} por {self.trainer.name} el {self.review_date}"




