from django.shortcuts import render

from django.http import HttpResponse


def finanace(request):

    data = Student.objects.all()

    context = {'allstudents': data}
    return render(request,'adm/hunt.html',context)


def stafffinanace(request):
    return render(request,'finance/given.html')
