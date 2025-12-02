from django.contrib import admin
from django.utils.html import format_html
from .models import Coach, Player, JoinRequest



@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'education', 'qualification', 'work_start_year', 'photo_preview', 'order',)
    list_filter = ('position', 'qualification')
    search_fields = ('full_name', 'position', 'qualification')
    list_editable = ('order',)  # можно менять прямо в списке
    ordering = ('order',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('full_name', 'position')
        }),
        ('Профессиональные данные', {
            'fields': ('qualification', 'education', 'work_start_year')
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

@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ('parent_full_name', 'child_full_name', 'branch', 'created_at')
    search_fields = ('parent_full_name', 'child_full_name', 'parent_phone')
    list_filter = ('branch', 'created_at')
    ordering = ['-created_at']