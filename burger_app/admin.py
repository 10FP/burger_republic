from django.contrib import admin
from .models import Hamburger, Subscriber, MenuHamburger, Contact, MenuFries, MenuDrink

# Register your models here.


class HamburgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'price', 'image')

class MenuHamburgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

class MenuFriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

class MenuDrinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on')
    search_fields = ('email', 'subscribed_on')
    list_filter = ('email', 'subscribed_on')

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")



admin.site.register(Hamburger, HamburgerAdmin)
admin.site.register(MenuHamburger, MenuHamburgerAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(MenuDrink, MenuDrinksAdmin)
admin.site.register(MenuFries, MenuFriesAdmin)