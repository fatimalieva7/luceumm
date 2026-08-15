from django.shortcuts import render

from .models import Profession, Pedagog, Courses, About, InstitutionHistory,  Achievement, BookCategory, Book, LibraryEvent, DigitalResource,DormitoryFeature,DormitoryRoom,DormitoryRule,DormitoryFAQ



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

def library_view(request):
    books = Book.objects.filter(is_available=True).select_related('category')
    digital_resources = DigitalResource.objects.all()
    events = LibraryEvent.objects.all().order_by('-event_date')[:4]

    context = {
        'books': books,
        'digital_resources': digital_resources,
        'events': events,
    }
    return render(request, 'content/libery.html', context)

def studenthome(request):
     context = {
        "features": DormitoryFeature.objects.all(),
        "rooms": DormitoryRoom.objects.filter(is_active=True),
        "rules": DormitoryRule.objects.all(),
        "faqs": DormitoryFAQ.objects.all(),
    }
     return render (request, 'content/studenthome.html',context)
