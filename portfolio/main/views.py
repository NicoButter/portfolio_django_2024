# main/views.py
from django.shortcuts import render, redirect
from .models import AboutMe, Skill, Project
from .forms import AboutMeForm, SkillForm, ProjectForm
from django.contrib.auth.decorators import login_required

def home(request):
    about_me = AboutMe.objects.filter(user=request.user).first()
    skills = Skill.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    return render(request, 'main/home.html', {
        'about_me': about_me,
        'skills': skills,
        'projects': projects,
    })

@login_required
def edit_about_me(request):
    about_me = AboutMe.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = AboutMeForm(request.POST, instance=about_me)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AboutMeForm(instance=about_me)
    return render(request, 'main/edit_about_me.html', {'form': form})

@login_required
def edit_skill(request, skill_id):
    skill = Skill.objects.get(id=skill_id, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'main/edit_skill.html', {'form': form})

@login_required
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/edit_project.html', {'form': form})
