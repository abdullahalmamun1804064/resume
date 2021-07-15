from django import forms
from django.forms import fields, widgets
from .models import uregi
GENDER_CHOICE=[
    ('Male','Male'),
    ('Female','Female')
]
STATE_CHOICE=[
    ('Bangaladesh','bangladesh'),
    ('India','India'),
    ('Nepal','Nepal'),
    ('USA','USA'),
    ('Gana','Gana'),
    ('Urogo','Urogo')
]
JOB_CITY=[
    ('Dhaka','Dhaka'),
    ('Comilla','Comilla'),
    ('Dilli','Dilli'),
    ('katmondo','katmondo'),
    ('Sikago','Sikago')
]
class uregi_forms(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    state=forms.ChoiceField(choices=STATE_CHOICE,widget=forms.Select(attrs={'class':'form-select'}))
    job=forms.MultipleChoiceField(label='Prefect Job Location',choices=JOB_CITY,widget=forms.CheckboxSelectMultiple())
    class Meta:
        model=uregi
        fields=['name','dob','gender','locality','city','pin','state','mobile','email','job','profile_image','doc']
        labels={
            'name':'Full Name','dob':'Date of Birth','pin':'Post Code','mobile':'Mobile Number','email':'Email Address','job':'Job location','profile_image':'Profile Image','doc':'documentation'

        }

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }