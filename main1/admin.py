from django.contrib import admin
from . models import Tutorial
from tinymce.widgets import TinyMCE # type: ignore
from django.db import models



# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    widgets = {
        'tutorial_content': TinyMCE(attrs={'cols': 80, 'rows': 30},
                                     mce_attrs={'plugins': 'codesample',
                                                'toolbar': 'codesample'}),
    }
    fieldsets = [
                 ("Title/date", {"fields":["tutorial_title", "tutorial_published"]}),
                 ("Content", {"fields":["tutorial_content"]})
                ]
    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }
admin.site.register(Tutorial, TutorialAdmin)
