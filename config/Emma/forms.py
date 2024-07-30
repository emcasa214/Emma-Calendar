from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'list']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['list'].queryset = List.objects.filter(user=user)
        else:
            self.fields['list'].queryset = List.objects.none()

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'color']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }

class TaskSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Tìm kiếm')
    list = forms.ModelChoiceField(queryset=List.objects.none(), required=False)
    completed = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskSearchForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['list'].queryset = List.objects.filter(user=user)

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['remind_at', 'repeat']
        widgets = {
            'remind_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
