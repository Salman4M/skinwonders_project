from .models import Vacancies,ContactUs,Blog
from modeltranslation.translator import TranslationOptions,register

@register(Vacancies)
class VacanciesTranslationOptions(TranslationOptions):
    fields=("jobtitle","location","department")

@register(ContactUs)
class ContactUsTranslationOption(TranslationOptions):
    fields=('subject',)

@register(Blog)
class BlogTranslationOption(TranslationOptions):
    fields=('date','type')
