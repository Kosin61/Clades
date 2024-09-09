from django.contrib import admin

from django.contrib import admin
from .models import contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display=('name','email','message','submitted_at')
  search_fields=('name','email')
# Register your models here.
