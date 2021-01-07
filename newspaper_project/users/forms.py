from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):#CreateViewForm
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields =  ('username','email','age','phone',)#UserCreationForm.Meta.fields + ('age','phone',)
    
class CustomUserChangeForm(UserChangeForm):#UpdateViewForm

    class Meta:
        model = CustomUser
        fields = ('username','email','age','phone',)#UserChangeForm.Meta.fields 
