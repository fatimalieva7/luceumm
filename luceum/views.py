from django.shortcuts import render
from .models import Cotegory, HeroSection

def news(request):
    return render(request, 'luceum/news.html')

def index(request):

    context = {
        'hero': HeroSection.objects.all(),

        'categories': Cotegory.objects.all(),
    }

    return render(request, 'luceum/index.html',context)



def contact(request):
    return render(request, 'luceum/contact.html')


def testimonial(request):
    return render(request, 'luceum/testimonial.html')

def page_not_found(request, exception):
    return render(request, 'luceum/404.html', status=404)



