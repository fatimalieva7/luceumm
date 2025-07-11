from django.shortcuts import render


def index(request):
    return render(request, 'luceum/index.html')
def about(request):
    return render(request, 'luceum/about.html')

def contact(request):
    return render(request, 'luceum/contact.html')

def courses(request):
    return render(request, 'luceum/courses.html')

def team(request):
    return render(request, 'luceum/team.html')

def testimonial(request):
    return render(request, 'luceum/testimonial.html')


