from django import forms
from .models import Room, Sign, Project

'''
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        name = forms.CharField(max_length=50,
            widget = forms.TextInput (
                attrs ={'placeholder': 'Enter Project Name', 'label': 'Project Name', 'size':'50' } ))

        contact = forms.CharField(max_length=50,
            widget = forms.TextInput(
                attrs = { 'placeholder': 'Name of main contact' , 'size':'50'  } ))


        add1    = forms.CharField(widget=forms.TextInput(attrs={'size':'75' , 'label':'Address'})) 
        add2    = forms.CharField(widget=forms.TextInput(attrs={'size':'75' , 'label': '' }))
        post_code = forms.CharField(widget=forms.TextInput(attrs={'size':'15' , 'label':'Postcode'}))
        tel     = forms.CharField(widget=forms.TextInput(attrs={'size':'15' , 'label': 'Phone Number' }))
        email = forms.CharField(widget=forms.TextInput(attrs={'size':'75' , 'label': 'Email' }))


'''

#class ProjectForm(forms.Form):

class ProjectForm(forms.Form):
        name = forms.CharField(max_length=50, label='Project Name',
                widget = forms.TextInput ( attrs ={ 'placeholder': 'Enter Project Name'} ))    

        contact = forms.CharField ( max_length=50, label='Contact Name', 
                widget=forms.TextInput(attrs={'placeholder':'Person to contact' }) ) 

        add1 = forms.CharField( max_length = 100, label='Address',
                widget=forms.TextInput(attrs={ 'placeholder':'Address'})) 

        add2 = forms.CharField(max_length=100, label='',
                widget=forms.TextInput(attrs={'label': '' }))

        post_code = forms.CharField(max_length=10)

        tel = forms.CharField(max_length=15, label='Telephone No.',
                widget=forms.TextInput(attrs={'placeholder':'mobil / landline'}))

        email = forms.CharField(max_length=50)

        start_date = forms.DateField( widget = forms.DateInput(
                attrs = { 'placeholder':'Enter date YYYY-MM-DD' , 'class':'datepicker'} ))

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ( 'project', 'total', 'room_type' , 'room_size' , 'img' ) 

class getProjectForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('project',)

class SignForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields ='signature',


