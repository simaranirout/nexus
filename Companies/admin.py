from django.contrib import admin
from .models import Companies
# Register your models here.
@admin.register(Companies)
class UserAdmin(admin.ModelAdmin):
    list_display = ('cid','name','city','zipcode')