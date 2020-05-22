from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class PpicForm(ModelForm):
    class Meta:
        model= profile
        fields=['ppic']

class BpicForm(ModelForm):
    class Meta:
        model= profile
        fields=['bpic']
class AdrpicForm(ModelForm):
    class Meta:
        model= profile
        fields=['adrfpic','adrbic']
