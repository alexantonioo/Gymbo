from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ClientProfile, TrainerProfile

class ClientSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        if commit:
            user.save()
        ClientProfile.objects.create(user=user, name=self.cleaned_data.get('name'))
        return user

class TrainerSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_trainer = True
        if commit:
            user.save()
        TrainerProfile.objects.create(user=user, name=self.cleaned_data.get('name'))
        return user
