from django.contrib import admin
from .models import ContactMail

# Register your models here.

class ContactMailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)

admin.site.register(ContactMail, ContactMailAdmin)
