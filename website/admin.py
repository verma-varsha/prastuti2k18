from django.contrib import admin
from .models import Event, Team

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('Name',)}

admin.site.register(Event, EventAdmin)
admin.site.register(Team)