from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'surname', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)