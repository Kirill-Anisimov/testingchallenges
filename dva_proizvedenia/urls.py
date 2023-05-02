from django.urls import path

from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("proizvedenie", views.proizvedenie, name="proizvedenie"),
	path("uspeh", views.uspeh, name="uspeh"),
	path("neudacha", views.neudacha, name="neudacha"),
]
