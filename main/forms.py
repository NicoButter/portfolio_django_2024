from django import forms
from .models import AboutMe, Skill, Development

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['bio']

# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Skill
#         fields = ['name', 'description', 'image', 'progress']

class SkillForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = Skill
        fields = ['name', 'description', 'image_file', 'progress']

    def save(self, commit=True):
        instance = super(SkillForm, self).save(commit=False)
        if self.cleaned_data.get('image_file'):
            instance.image = self.cleaned_data['image_file'].read()
        if commit:
            instance.save()
        return instance

class DevelopmentForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = Development
        fields = ['title', 'description', 'image_file']

    def save(self, commit=True):
        instance = super(DevelopmentForm, self).save(commit=False)
        if self.cleaned_data.get('image_file'):
            instance.image = self.cleaned_data['image_file'].read()
        if commit:
            instance.save()
        return instance
    

