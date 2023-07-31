from django.urls import path


from administration.views import *

urlpatterns = [
    path('new-admin',addAdmission),
    path('admreport',allstudents)
]