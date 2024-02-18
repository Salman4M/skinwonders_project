from django.contrib import admin

# Register your models here.

from .models import ContactUs,Vacancies,CV,Blog

from modeltranslation.admin import TranslationAdmin

@admin.register(Vacancies)
class VacanciesAdmin(TranslationAdmin):
    list_display=('jobtitle',)

@admin.register(ContactUs)
class ContactUsAdmin(TranslationAdmin):
    list_display=('subject',)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display=('title',)
# admin.site.register(ContactUs)
# admin.site.register(Vacancies)
admin.site.register(CV)
# admin.site.register(Blog)


