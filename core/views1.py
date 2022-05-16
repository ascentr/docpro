from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                        CreateView, UpdateView, DeleteView)
from .forms import RoomForm, SignForm, ProjectForm
#from core.models import Room, Project, Sign
from core import models

import os
from PIL import Image, ImageDraw, ImageFont
import math

# Create your views here.
'''
class ProjectCreateView(CreateView):
    fields = ( 'name', 'contact' , 'add1' , 'add2' , 'post_code' ,  'tel' , 'email' )
    model = models.Project
'''

def ProjectCreateView(request):
    from core.models import Project
    form = ProjectForm(request.POST)

    if request.method=='POST':
        if form.is_valid():            
            new_project = Project(  
                name = request.POST['name'], 
                contact = request.POST['contact'], 
                add1 = request.POST['add1'], 
                add2 = request.POST['add2'], 
                post_code = request.POST['post_code'],  
                tel = request.POST['tel'], 
                email = request.POST['email']   
                )

            new_project.save()
        return redirect('/core/projectlist' )
    else:
        form =ProjectForm()

    return render(request,  'create_project.html',{
        'form':form
    })


class ProjectListView(ListView):
    context_object_name = "projects"
    model = models.Project

class ProjectDetailView(DetailView):
    context_object_name = "project_details"
    model = models.Project
#    template_name = 'basic_app/school_detail.html'

class ProjectUpdateView(UpdateView):
    fields = ( 'name', 'contact' , 'add1' , 'add2' , 'post_code' ,  'tel' , 'email' )
    model = models.Project

class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy("projectlist")

def room_list(request):
    from core.models import Room
    rooms = Room.objects.all()
    return render(request, 'room_list.html' , {
        'rooms':rooms
    })

def create_room(request):

    if request.method=='POST':
        form = RoomForm(request.POST, request.FILES)

        my_type = request.POST['room_type']
        my_img_file = request.FILES['img']
#        my_project = request.POST.get('project.value')
#        my_project = str(request.POST.get('project'))
        my_project = request.POST.get('project')#        print(my_type)
        if form.is_valid():
#            form.save()
#            print ("project "  + str(my_project) )
            print(my_project)
            initial_obj = form.save(commit=False)
            initial_obj.save()
            saved_file = initial_obj.img.url

#remove slash from the start of the url string
            saved_file = saved_file[1:]
            my_image = Image.open(saved_file)

#resize for A4 width at 96dpi i.e 794 pixels max
            my_width = my_image.size[0]
            my_height = my_image.size[1]

            string = my_type

            if  my_width > 780:
                temp = 780 / my_width
                new_height = temp * my_height
                new_height = int(float(new_height))                
                new_width = 780
                string = my_type + '\n I am resized'

                new_size = (new_width , new_height)
                my_resized_image = my_image.resize(new_size)
                my_image = my_resized_image
   
            shape = [(0, 0), (250, 60)]
            img1 = ImageDraw.Draw(my_image)
            img1.rectangle(shape, fill ="#fff", outline="#0a2d12")

            #write some text in the rectangle
            draw = ImageDraw.Draw(my_image)
            myfont = ImageFont.truetype("calibrib.ttf", 20)
            points = 10,20

            draw.text(points, string, "#000", font=myfont  )
            my_image.save(saved_file)

            return redirect('/core/roomlist' )
    else:
        form =RoomForm()

    return render(request,  'create_room.html',{
        'form':form
    })

