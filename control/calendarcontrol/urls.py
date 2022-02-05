"""control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from calendarcontrol import views
from .views import EventDetailView, pdf_view, EventUpdateView, EventDeleteView

urlpatterns = [
  path('', views.index, name='index'),
  path('event/<int:pk>/',EventDetailView.as_view(), name="event-detail"),
  path('pdf_view/<int:pk>/', views.pdf_view, name='pdf-view'),
  path('update/<int:pk>/', EventUpdateView.as_view(), name='event-update'),
  path('delete/<int:pk>/', EventDeleteView.as_view(), name='event-delete'),
  path('test/<int:pk>/', views.test, name='test'),




]
