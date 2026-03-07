from django.contrib import admin
from .models import Project, Room

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'post_code', 'city', 'start_date', 'completed')
  

class RoomAdmin(admin.ModelAdmin):
  list_display = ('room_type', 'project')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Room, RoomAdmin)
  