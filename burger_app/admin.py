from django.contrib import admin
from .models import Hamburger

# Register your models here.


class HamburgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'price', 'image')


admin.site.register(Hamburger, HamburgerAdmin)