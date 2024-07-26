from django.shortcuts import render, redirect
from .models import AboutMe, Skill, Development
from .forms import AboutMeForm, SkillForm, DevelopmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    about_me = AboutMe.objects.first()
    skills = Skill.objects.all()
    developments = Development.objects.all()
    
    context = {
        'about_me': about_me,
        'skills': skills,
        'developments': developments,
    }
    return render(request, 'main/home.html', context)

@login_required
def edit_about_me(request):
    about_me, created = AboutMe.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AboutMeForm(request.POST, instance=about_me)
        if form.is_valid():
            about_me = form.save(commit=False)
            about_me.user = request.user
            about_me.save()
            return redirect('home')
    else:
        form = AboutMeForm(instance=about_me)
    return render(request, 'main/edit_about_me.html', {'form': form})

@login_required
def edit_skill(request, skill_id):
    skill = Skill.objects.get(id=skill_id, user=request.user)
    
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            skill.delete()
            return redirect('home')
        
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'main/edit_skill.html', {'form': form})

@login_required
def edit_development(request, development_id):
    development = Development.objects.get(id=development_id, user=request.user)
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            development.delete()
            return redirect('home')
               
        form = DevelopmentForm(request.POST, request.FILES, instance=development)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DevelopmentForm(instance=development)
    return render(request, 'main/edit_development.html', {'form': form})

@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('home')  
    else:
        form = SkillForm()
    return render(request, 'main/add_skill.html', {'form': form})

@login_required
def add_development(request):
    if request.method == 'POST':
        form = DevelopmentForm(request.POST, request.FILES)
        if form.is_valid():
            development = form.save(commit=False)
            development.user = request.user
            development.save()
            return redirect('home')
    else:
        form = DevelopmentForm()
    return render(request, 'main/add_development.html', {'form': form})

