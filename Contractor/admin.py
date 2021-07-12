from django.contrib import admin
from .models import Contractor
# Register your models here.
@admin.register(Contractor)
class UserAdmin(admin.ModelAdmin):
    list_display = ('cid','name','city','zipcode')