from django.contrib import admin
<<<<<<< Updated upstream
=======
from .models import User, ClientProfile, TrainerProfile, Exercise

# Configuración para User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_client', 'is_trainer', 'is_staff', 'is_active')
    list_filter = ('is_client', 'is_trainer', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# Configuración para ClientProfile
@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'active', 'trainer', 'age', 'height')
    list_filter = ('active', 'trainer', 'age', 'height')
    search_fields = ('name', 'user__username', 'user__email', 'trainer__user__username')
    filter_horizontal = ('exercises',)  # Añadir la interfaz de selección horizontal para ejercicios

# Configuración para TrainerProfile
@admin.register(TrainerProfile)
class TrainerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'user__username', 'user__email')

# Configuración para Exercise
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'exercise_type', 'body_part', 'level', 'rating', 'date', 'is_done')
    list_filter = ('exercise_type', 'body_part', 'level', 'date', 'is_done')
    search_fields = ('title', 'description', 'body_part')
>>>>>>> Stashed changes
