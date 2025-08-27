from django.contrib import admin
from .models import  (Profession, Pedagog, Bestpedagog, Courses, About,
                      InstitutionHistory,  Achievement)



admin.site.register(Profession)
admin.site.register(InstitutionHistory)

admin.site.register(Achievement)

admin.site.register(Pedagog)

admin.site.register(Bestpedagog)

admin.site.register(Courses)

admin.site.register(About)