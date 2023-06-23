from cProfile import label
from tkinter import Label, Widget
from django import forms
from .models import *

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICE=[
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Varanasi','Varanasi'),
    ('Mumbai','Mumbai'),
    ('Banglore','Banglore')
]
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    # job_city=forms.MultipleChoiceField(label='Prefered Job Locations',choices=JOB_CITY_CHOICE)    // WORKING DIFFERENCE
    job_city=forms.MultipleChoiceField(label='Prefered Job Locations',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city','pin','state','mobile','email','job_city','experience','education','projects','skills','awards','languages','profile_image','my_file']
        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin code','mobile':'Mobile No','email':'Email Id','profile_image':'Profile Image','my_file':'Document','Experience':'experience','Higher Education':'education','Projects':'projects','skills':'Skills','Awards':'awards','Languages':'languages'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'experience':forms.TextInput(attrs={'class':'form-control'}),
            'education':forms.Textarea(attrs={'class':'form-control'}),
            'projects':forms.Textarea(attrs={'class':'form-control'}),
            'skills':forms.TextInput(attrs={'class':'form-control'}),
            'awards':forms.TextInput(attrs={'class':'form-control'}),
            'languages':forms.TextInput(attrs={'class':'form-control'}),
        }
