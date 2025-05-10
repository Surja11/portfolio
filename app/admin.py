from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  class Meta:
    model = Contact
    fields = '__all__'

  list_display = ['email', 'message']

class ProjectAdmin(admin.ModelAdmin):
  class Meta:
    model = Project
    field = '__all__'

  list_display = ['name','tech_used','link']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)