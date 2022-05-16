from django.db import models
from django.urls import reverse
import os
import django.utils.timezone


def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    return '{add}/{basename}{ext}'.format(add=instance.project, basename= basefilename, ext= file_extension)
#    return '{add}/{room}/{basename}{ext}'.format(add=instance.project, room=instance.room_type, basename= basefilename, ext= file_extension)
    my_room = Room.room_type

#def upload_image_to(instance, filename):
#    return '{}/{}'.format(instance.room.project, filename)

#class Image(models.Model):
#    project = models.ForeignKey(Project, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to=upload_image_to)

class Project(models.Model):
    name = models.CharField( max_length=50, null= False, blank=True, default= 'temp')  # change to false on production
    contact = models.CharField( max_length=50, null=False, blank=False )
    add1 = models.CharField( max_length=100, null=False, blank=False )
    add2 = models.CharField( max_length=100, null=True, blank=True )
    post_code = models.CharField( max_length=10, null=False, blank=False )
    tel = models.CharField( max_length=13, null=False, blank=False )
    email = models.CharField( max_length=50, null=False, blank=False )
    start_date = models.DateField( auto_now=True, auto_now_add=False )

    def __str__(self):
        return self.name
#        return self.name.strip()
#        return self.cleaned_data['name'].strip()
#string.replace(" ", "") 


    def get_absolute_url(self):
        return reverse("projectdetail", kwargs={'pk':self.pk})

class Room(models.Model):
    project = models.ForeignKey(Project,  related_name='rooms', on_delete=models.CASCADE, default="eg")
    total =models.IntegerField()
    room_type = models.CharField( max_length=50)  # i.e bedroom /living room etc
    room_size = models.CharField( max_length=50)
    img = models.ImageField( upload_to=photo_path, null=True, blank=True)

    def __str__(self):
        return self.room_type

class Sign(models.Model):
    signature = models.ImageField(upload_to='my_Add/signature', height_field=None, width_field=None, max_length=None,  null=True, blank=True)
    
    def __str__(self):
        return self.signature


