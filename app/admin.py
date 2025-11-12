from django.contrib import admin
from django.utils.html import format_html
from .models import Coach, Player, Parent


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'qualification', 'work_start_year', 'photo_preview')
    list_filter = ('position', 'qualification')
    search_fields = ('full_name', 'position', 'qualification')
    ordering = ('full_name',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('full_name', 'position')
        }),
        ('Профессиональные данные', {
            'fields': ('qualification', 'work_start_year')
        }),
        ('Фотография', {
            'fields': ('photo', 'photo_preview'),
            'description': 'Загрузите фотографию тренера. Поддерживаются форматы: JPG, PNG, GIF.'
        }),
    )
    
    readonly_fields = ('photo_preview',)
    
    def photo_preview(self, obj):
        """Превью фотографии в админке"""
        if obj.photo:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px; border-radius: 4px;" />',
                obj.photo.url
            )
        return format_html('<span style="color: #999;">Фотография не загружена</span>')
    
    photo_preview.short_description = 'Превью фотографии'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'age', 'coach', 'photo_preview')
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
            'fields': ('photo', 'photo_preview'),
            'description': 'Загрузите фотографию игрока. Поддерживаются форматы: JPG, PNG, GIF.'
        }),
    )
    
    readonly_fields = ('photo_preview',)
    
    def photo_preview(self, obj):
        """Превью фотографии в админке"""
        if obj.photo:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px; border-radius: 4px;" />',
                obj.photo.url
            )
        return format_html('<span style="color: #999;">Фотография не загружена</span>')
    
    photo_preview.short_description = 'Превью фотографии'


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