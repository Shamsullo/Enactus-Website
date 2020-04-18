from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import *

# Register your models here.

admin.site.register(Welcome)

admin.site.register(AboutEnactus)


admin.site.register(Projects)
admin.site.register(AcademicAdvisors)
admin.site.register(Contact)
admin.site.register(Partners)

@admin.register(AboutEnactus)
class AboutEnactusAdmin(TranslationAdmin):
    list_display = ("title", "url")


@admin.register(Projects)
class ProjectsAdmin(TranslationAdmin):
    list_display = ("name", "url")
    
@admin.register(AcademicAdvisors)
class AcademicAdvisorsAdmin(TranslationAdmin):
    list_display = ("f_name", "url")
    
