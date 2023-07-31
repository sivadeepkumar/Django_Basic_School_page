from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'index.html')




# Create your views here.
def addAdmission(request):
    context = {'name':'aryan'}
    return render(request,'adm/openadmissions.html',context)



def allstudents(request):
   
    return render(request,'finance/allstudents.html')