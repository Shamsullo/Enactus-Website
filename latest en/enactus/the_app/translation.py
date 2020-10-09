
from modeltranslation.translator import register, TranslationOptions
from .models import Welcome, AboutEnactus, Gallery, Projects, AcademicAdvisors, Contact


@register(Welcome)
class WelcomeTranslationOptions(TranslationOptions):
    fields = ('text_under_welcome',)


@register(AboutEnactus)
class AboutEnactusTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


# @register(Gallery)
# class GallerryTranslationOptions(TranslationOptions):
#     fields = ('caption')


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('name', 'short_desc', 'description')


@register(AcademicAdvisors)
class AcademicAdvisorsTranslationOptions(TranslationOptions):
    fields = ('f_name', 'l_name', 'position')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address',)
