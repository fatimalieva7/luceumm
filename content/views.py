from django.shortcuts import render

from .models import Profession, Pedagog, Bestpedagog, Courses, About, InstitutionHistory,  Achievement



def team(request):
    return render(request, 'content/team.html')

def courses(request):
    context = {
    'courses': Courses.objects.all(),
    }
    return render(request, 'content/courses.html',context)

def about(request):
        context = {
            'professions': Profession.objects.all(),
            'about': About.objects.all(),
            'pedagogs': Pedagog.objects.all(),
            'best_pedagogs': Bestpedagog.objects.all(),
            'histories': InstitutionHistory.objects.all(),
            'achievements': Achievement.objects.all(),
        }
        return render(request, 'content/about.html', context)

