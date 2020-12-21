"""Cure_Dental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from Doctors.views import doctors_view
from Patients_Cases.views import cases_view
from Branches.views import branches_view
from Booking.views import booking_handler
from Feedback.views import feedback_handler
from Consultation.views import consultation_handler
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Doctors/View', doctors_view),
    path('Cases/View', cases_view),
    path('Branches/View', branches_view),
    path('Booking/Create-New-Booking', booking_handler),
    path('Feedback/Create-New-Feedback',feedback_handler),
    path('Consultation/Create-New-Consultation', consultation_handler)
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)