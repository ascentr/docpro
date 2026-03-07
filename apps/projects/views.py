from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, 
  CreateView, UpdateView, DeleteView)
import os
import math
from PIL import Image, ImageDraw, ImageFont
from django.contrib import messages
from .forms import ProjectForm, RoomForm
from .models import Project, Room
from .utils import get_gps_from_image, process_image


def ongoing_projects(request):
  projects = Project.objects.filter(completed=False)
  
  return render(request, "projects/ongoing.html", {"projects":projects})

def completed_projects(request):
  projects =  Project.objects.filter(completed=True)
  
  return render(request, "projects/completed.html", {"projects":projects})


class ProjectListView(ListView):
  model = Project
  context_object_name = 'projects'
  response_template = "projects/project_list.html"


class CreateProjectView(CreateView):
  model = Project
  form_class = ProjectForm
  
  def get_success_url(self):
    return reverse(
      'createroom', 
      kwargs={"pk": self.object.id})

  
class ProjectDetailView(DetailView):
  
  model = Project
  template_name = "projects/project_detail.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    project = self.object
    context["rooms"] = project.rooms.all()    
    context["can_add_room"] = project.can_add_room

    return context
  
  
class ProjectUpdateView(UpdateView):
  model = Project
  form_class = ProjectForm
  template_name = "projects/project_form.html"
  
  def get_success_url(self):
    return reverse(
      "projects"
    )
    # return reverse(
    #   "createroom",
    #   kwargs={"pk": self.object.id}
    # )  
  
  
def create_room(request, pk):
  project = Project.objects.get(id=pk)

  form = RoomForm(request.POST, request.FILES)
  if request.method == 'POST':

    # Use room_type to print room type on the image 
    room_type = request.POST['room_type'] 
    if form.is_valid():
      room = form.save(commit=False)
      room.project = project
      room.save()
      
      saved_file = room.photo.path
      
      lat, lon = get_gps_from_image(saved_file)
      print("latitude & longitude",lat, lon)
      
      if lat and lon:
        room.latitude = lat
        room.longitude = lon
        room.save(update_fields=["latitude", "longitude"])
      
      process_image(
        image_path = room.photo.path,
        project = project.name,
        room_type = room.room_type,
        lat=lat,
        lon=lon,
      )
      
      return redirect("projectdetail", pk=project.pk)
  else:    
    form = RoomForm()
  context = {
    'form':form,
    'project':project
  }    
  return render(request, "projects/create_room.html", context )


def update_room(request, project_id, room_id):

  project = get_object_or_404(Project, id=project_id) 
  room = get_object_or_404( Room, id=room_id, project=project)
  
  if request.method == 'POST':
    form = RoomForm(request.POST, request.FILES, instance=room)
    
    if form.is_valid():
      form.save()

      if 'photo' in form.changed_data:

        lat, lon = get_gps_from_image(room.photo.path)
        print("latitude & longitude",lat, lon)
        
        if lat and lon:
          room.latitude = lat
          room.longitude = lon
          room.save(update_fields=["latitude", "longitude"])
        
          process_image(
            image_path = room.photo.path,
            project = project.name,
            room_type = room.room_type,
            lat=lat,
            lon=lon,
          )
      return redirect('projectdetail', pk=project.id)

  else:
    form = RoomForm(instance=room)
    
  return render(
    request, 
    'projects/update_room.html',
    {
      'form':form,
      'project': project,
      'room': room,
    }
  )

def complete_project(request, project_id):
  
  if request.method=="POST":    
    project = get_object_or_404(Project, id=project_id) 
    project.completed = True
    project.save()

    messages.success(request, "Project completed successfully.")

  return redirect("projectdetail", pk=project_id)


class DeleteRoomView(DeleteView):
  model = Room
  template_name = "projects/room_confirm_delete.html"
  
  def get_object(self):
    return Room.objects.get(
      id=self.kwargs["room_id"],
      project_id=self.kwargs["project_id"]
    )
  
  def get_success_url(self):
    return reverse(
      "projectdetail",
      kwargs={"pk":self.kwargs['project_id']}
    )