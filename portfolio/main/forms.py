from django import forms
from .models import AboutMe, Skill, Development

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['bio']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description', 'image', 'progress']

class DevelopmentForm(forms.ModelForm):
    class Meta:
        model = Development
        fields = ['title', 'description', 'image']
        