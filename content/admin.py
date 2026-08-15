from django.contrib import admin
from .models import  (Profession, Pedagog,  Courses, About,
                      InstitutionHistory,  Achievement,BookCategory, Book, LibraryEvent, DigitalResource ,
                      DormitoryFeature,
                        DormitoryRoom,
                        DormitoryRule,
                        DormitoryFAQ,)







admin.site.register(Profession)
admin.site.register(InstitutionHistory)

admin.site.register(Achievement)

admin.site.register(Pedagog)

admin.site.register(Courses)

admin.site.register(About)

admin.site.register(Book)
admin.site.register(LibraryEvent)
admin.site.register(DigitalResource)
admin.site.register(BookCategory)

admin.site.register(DormitoryFAQ)
admin.site.register(DormitoryFeature)
admin.site.register(DormitoryRoom)
admin.site.register(DormitoryRule)