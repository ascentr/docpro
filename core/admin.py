from django.contrib import admin

# Register your models here.
from core.models import Project, Room, Sign

admin.site.register(Project)
admin.site.register(Room)
admin.site.register(Sign)
