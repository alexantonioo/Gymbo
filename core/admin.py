from django.contrib import admin
from .models import Exercise
from .models import User, Trainer, Client

# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'exercise_type', 'body_part', 'equipment', 'level', 'rating')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'role', 'is_active')
    list_filter = ('role', 'is_active')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'trainer')
    filter_horizontal = ('exercises',)