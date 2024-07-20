# main/forms.py
from django import forms
from .models import AboutMe, Skill, Project

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['bio']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']
