from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


class ProjectAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description_ru = forms.CharField(
        label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(
        label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Projects
        fields = '__all__'


admin.site.register(Welcome)

# admin.site.register(Projects)
# admin.site.register(AcademicAdvisors)
admin.site.register(Contact)
admin.site.register(Partners)


@admin.register(AboutEnactus)
class AboutEnactusAdmin(TranslationAdmin):
    list_display = ("title", "text", "get_image", "id")
    list_display_links = ("title", "text")

    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'< img src={obj.photo.url} width="60">')

    get_image.short_description = "Изображение"

# commenet
# admin.site.register(AboutEnactus, AboutEnactusAdmin)


@admin.register(Projects)
class ProjectsAdmin(TranslationAdmin):
    list_display = ("name", "id")
    form = ProjectAdminForm


@admin.register(AcademicAdvisors)
class AcademicAdvisorsAdmin(TranslationAdmin):
    list_display = ("photo", "f_name", "l_name", "id")
    list_display_links = ("f_name", "l_name")


admin.site.site_title = "AUCA Enactus Website Administration"
admin.site.site_header = "AUCA Enactus Website Administration"
