from django.contrib import admin
from . models import Section

# Register your models here.
class SectionAdmin(admin.ModelAdmin):
	list_display = ('title', 'section')

admin.site.register(Section, SectionAdmin)