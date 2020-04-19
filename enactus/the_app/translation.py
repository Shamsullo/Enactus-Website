
from modeltranslation.translator import register, TranslationOptions
from .models import AboutEnactus, Projects, AcademicAdvisors

AboutEnactus


@register(AboutEnactus)
class AboutEnactusTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(AcademicAdvisors)
class AcademicAdvisorsTranslationOptions(TranslationOptions):
    fields = ('f_name', 'l_name', 'position', 'desc')
