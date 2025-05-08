from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  class Meta:
    model = Contact
    fields = '__all__'

admin.site.register(Contact, ContactAdmin)