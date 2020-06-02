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


# admin.site.register(Welcome)
admin.site.register(Message)
admin.site.register(Gallerry)
# admin.site.register(AcademicAdvisors)
# admin.site.register(Contact)
admin.site.register(Partners)


@admin.register(AboutEnactus)
class AboutEnactusAdmin(TranslationAdmin):
    list_display = ("title",)
    list_display_links = ("title",)

    # readonly_fields = ("get_image",)

    # def get_image(self, obj):
    #     return mark_safe(f'< img src={obj.photo.url} width="60">')

    # get_image.short_description = "Изображение"

# commenet
# admin.site.register(AboutEnactus, AboutEnactusAdmin)


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):

    class Meta:
        model = Projects
        fields = '__all__'


@admin.register(Welcome)
class WelcomeAdmin(TranslationAdmin):

    class Meta:
        model = Welcome
        fields = '__all__'


@admin.register(Projects)
class ProjectsAdmin(TranslationAdmin):
    list_display = ("name",)
    form = ProjectAdminForm


@admin.register(AcademicAdvisors)
class AcademicAdvisorsAdmin(TranslationAdmin):
    list_display = ("photo", "f_name", "l_name", "id")
    list_display_links = ("f_name", "l_name")


admin.site.site_title = "AUCA Enactus Website Administration"
admin.site.site_header = "AUCA Enactus Website Administration"
