from django.shortcuts import render
from .models import Cotegory, Profesion, Pedagog, Bestpedagog, Curss



def index(request):

    context = {
        'categories': Cotegory.objects.all(),
        'professions': Profesion.objects.all(),
        
        'best_pedagogs': Bestpedagog.objects.all(),
    }

    return render(request, 'luceum/index.html',context)
def about(request):
    context = {
        'categories': Cotegory.objects.all(),
        'professions': Profesion.objects.all(),
        
        'pedagogs': Pedagog.objects.all(),

        
    }
    return render(request, 'luceum/about.html',context)

def contact(request):
    return render(request, 'luceum/contact.html')

def courses(request):
    context = {
    'courses': Curss.objects.all(),
    }
    return render(request, 'luceum/courses.html',context)

def team(request):
    return render(request, 'luceum/team.html')

def testimonial(request):
    return render(request, 'luceum/testimonial.html')

def page_not_found(request, exception):
    return render(request, 'luceum/404.html', status=404)



