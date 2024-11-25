from django.contrib import admin
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


# Configuración para Exercise
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'exercise_type', 'body_part', 'level', 'rating', 'date', 'is_done')
    list_filter = ('exercise_type', 'body_part', 'level', 'date', 'is_done')
    search_fields = ('title', 'description', 'body_part')

# Configuración para TrainerProfile
@admin.register(TrainerProfile)
class TrainerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'active', "whatsapp_link", "get_clients")
    list_filter = ('active',)
    search_fields = ('name', 'user__username', 'user__email')

    # Función para mostrar los clientes de un entrenador
    def get_clients(self, obj):
        return ", ".join([client.name for client in obj.clients.all()])
    get_clients.short_description = 'Clientes'  # Esto establece el nombre de la columna

    # Filtro Many-to-Many de los clientes del entrenador
    filter_horizontal = ('clients',)

    # Se incluiría la opción de añadir, eliminar o editar clientes
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)



