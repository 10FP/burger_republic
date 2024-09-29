from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'burger_app'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("menu/", views.our_food, name="our_food"),
    path("contact/", views.contact, name="contact"),
    path('subscribe/', views.subscribe, name='subscribe'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)