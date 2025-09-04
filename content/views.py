from django.shortcuts import render

from .models import Profession, Pedagog, Courses, About, InstitutionHistory,  Achievement


def profession(request):
    context = {
    'professions': Profession.objects.all(),
    }
    return render(request, 'content/profession.html', context)


def team(request):
    context = {
    'pedagogs': Pedagog.objects.all(),
    }

    return render(request, 'content/team.html', context)

def courses(request):
    context = {
    'courses': Courses.objects.all(),
    }
    return render(request, 'content/courses.html',context)

def about(request):
        context = {
            'professions': Profession.objects.all(),
            'about': About.objects.all(),
            'histories': InstitutionHistory.objects.all(),
            'achievements': Achievement.objects.all(),
        }
        return render(request, 'content/about.html', context)

