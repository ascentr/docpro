from django.db import models
from django.urls import reverse
import os
import django.utils.timezone

# def photo_path(instance, filename):
#   basefilename, file_extention = os.path.splitext(filename)
#   print("basefilename",basefilename, "  extention =>", file_extention)
#   project_name = str(instance.project).replace(" ", "")
#   project_name = project_name.strip()
#   print("where the hell is it being saved => ",project_name+basefilename+file_extention)
  
#   return '{add}/{basename}{ext}'.format(add=project_name, basename=basefilename, ext=file_extention)

def photo_path(instance, filename):
    name, ext = os.path.splitext(filename)
    project = str(instance.project).replace(" ", "").strip()

    return f"projects/{project}/{name}{ext}"



class Project(models.Model):
    
  name = models.CharField( max_length=50, null= False, blank=True)  # change to false on production
  contact = models.CharField( max_length=50, null=False, blank=False )
  add1 = models.CharField( max_length=100, null=False, blank=False )
  add2 = models.CharField( max_length=100, null=True, blank=True )
  post_code = models.CharField( max_length=10, null=False, blank=False )
  city = models.CharField(max_length=125, null=True, blank=True)
  tel = models.CharField( max_length=13, null=False, blank=False )
  email = models.EmailField( max_length=50, null=False, blank=False )
  summary = models.TextField(null=True, blank=True)
  start_date = models.DateField()
  updated = models.DateField(auto_now=True)
  rooms_total = models.IntegerField()     #total number of rooms
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.name
  
  @property
  def can_add_room(self):
    return self.rooms.count() < self.rooms_total

  def get_absolute_url(self):
    return reverse("projectdetail", kwargs={'pk':self.pk})
  
  
class Room(models.Model):
  project = models.ForeignKey(Project,  related_name='rooms', on_delete=models.CASCADE)
  room_type = models.CharField( max_length=50)  # i.e bedroom /living room etc
  room_length = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
  room_width = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
  description = models.TextField(null=True, blank=True)
  photo = models.ImageField( upload_to=photo_path, null=True, blank=True)    
  latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
  longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
  
  def __str__(self):
    return self.room_type


class Sign(models.Model):
  project = models.ForeignKey(Project,  related_name='sign', on_delete=models.CASCADE)
  signature = models.ImageField(upload_to='{photo_path}/signature', height_field=None, width_field=None, max_length=None,  null=True, blank=True)
  
  def __str__(self):
    return self.signature

  
  