from django.contrib import admin
from .models import Coach, Player, Parent


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'qualification', 'work_experience')
    list_filter = ('position', 'qualification')
    search_fields = ('full_name', 'position', 'qualification')
    ordering = ('full_name',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('full_name', 'position')
        }),
        ('Профессиональные данные', {
            'fields': ('qualification', 'work_experience')
        }),
        ('Фотография', {
            'fields': ('photo',)
        }),
    )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'age', 'coach')
    list_filter = ('coach', 'birth_date')
    search_fields = ('full_name',)
    ordering = ('full_name',)
    raw_id_fields = ('coach',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('full_name', 'birth_date')
        }),
        ('Тренер', {
            'fields': ('coach',)
        }),
        ('Фотография', {
            'fields': ('photo',)
        }),
    )


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'player', 'player_birth_date')
    list_filter = ('player', 'created_at')
    search_fields = ('full_name', 'phone', 'player__full_name')
    ordering = ('full_name',)
    raw_id_fields = ('player',)
    
    fieldsets = (
        ('Информация о родителе', {
            'fields': ('full_name', 'phone')
        }),
        ('Связанный игрок', {
            'fields': ('player',),
            'description': 'Выберите игрока, для которого регистрируется родитель'
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')