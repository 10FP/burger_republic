from django.contrib import admin
from .models import Hamburger, Subscriber, MenuHamburger

# Register your models here.


class HamburgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'price', 'image')

class MenuHamburgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on')
    search_fields = ('email', 'subscribed_on')
    list_filter = ('email', 'subscribed_on')




admin.site.register(Hamburger, HamburgerAdmin)
admin.site.register(MenuHamburger, MenuHamburgerAdmin)
admin.site.register(Subscriber, SubscriberAdmin)