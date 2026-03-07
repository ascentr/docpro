from django import forms
from .models import Project, Room

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = (
      "name", "contact", "add1", "add2", "city", "post_code", 
      "tel", "email", "summary", "start_date", "rooms_total"
    )
    widgets = {
      "name": forms.TextInput(attrs={"placeholder": "Enter Project Name", "class":"form-control", "id":"floatingInput" }),
      "contact": forms.TextInput(attrs={"placeholder": "Person to contact", "class":"form-control", "id":"floatingInput"}),
      "add1": forms.TextInput(attrs={"placeholder": "Address", "class":"form-control"}),
      "add2": forms.TextInput(attrs={"placeholder": "Address", "class":"form-control"}),
      "city": forms.TextInput(attrs={"placeholder": "City", "class":"form-control"}),
      "post_code": forms.TextInput(attrs={"placeholder": "Post Code", "class":"form-control"}),      
      "tel": forms.NumberInput(attrs={"placeholder": "mobile / landline", "class":"form-control"}),
      "email":forms.EmailInput(attrs={"placeholder":"email", "class":"form-control"}),
      "summary":forms.Textarea(attrs={"placeholder":"i.e Boiler Upgrade", "class":"form-control"}),
      "start_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD", "type":"date" ,"class": "form-control datepicker " }),
      "rooms_total": forms.NumberInput(attrs={"placeholder": "Total Number of Rooms", "class": "form-control" }),
    }      
  
  
class RoomForm(forms.ModelForm):
  class Meta:
    model = Room

    fields = (  'room_type', 'room_length', 'room_width', 'description', 'photo') 
    widgets = {
      "room_type": forms.TextInput(attrs={"placeholder": "E.g Living Room / Bedroom etc.", "class":"form-control", "id":"floatingInput"}),
      "room_length": forms.NumberInput(attrs={"placeholder": "length in meters", "class":"form-control"}),
      "room_width": forms.NumberInput(attrs={"placeholder": "width in meters", "class":"form-control"}),
      "description": forms.Textarea(attrs={"placeholder": "e.g insulating os walls only", "class":"form-control"}),
      "photo": forms.FileInput(attrs={"class":"form-control"})
    }      


  # def __init__(self, *args, **kwargs):
  #   print("🔥 RoomForm __init__ called")
  #   super().__init__(*args, **kwargs)

  #   for name, field in self.fields.items():
  #     if field.__class__.__name__ == "CharField":
  #       widgets = {
  #         '${field.__class__.__name__}': forms.TextInput(attrs={"class":"form-control"})
  #       }
  # for field in fields:
  #   print(field)
        

# class SignForm(forms.ModelForm):
#   class Meta:
#     model = Sign
#     fields = ('project', 'signature')