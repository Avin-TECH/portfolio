from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Experience, Education, Contact

def home(request):
    projects = Project.objects.all()[:3]
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'skills': skills,
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {
        'projects': projects,
    })

def resume(request):
    experiences = Experience.objects.all().order_by('-start_date')
    education = Education.objects.all().order_by('-start_date')
    skills = Skill.objects.all()
    return render(request, 'portfolio/resume.html', {
        'experiences': experiences,
        'education': education,
        'skills': skills,
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Message sent! I will get back to you soon. ✅')
        return redirect('contact')
    return render(request, 'portfolio/contact.html')

def resume(request):
    experiences = Experience.objects.all().order_by('-start_date')
    education = Education.objects.all().order_by('-start_date')
    skills = Skill.objects.all()
    return render(request, 'portfolio/resume.html', {
        'experiences': experiences,
        'education': education,
        'skills': skills,
    })