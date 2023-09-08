from django.shortcuts import render
# from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_webpage(request):
    LTO = Topic.objects.all()
    d = {'LTO':LTO}
    if request.method =='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QSWO = Webpage.objects.all()
        d1 = {'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    LWO = Webpage.objects.all()
    d = {'LWO':LWO}
    if request.method == 'POST':
        # pk=request.POST['pk']
        pk=request.POST['na']
        dt=request.POST['dt']
        au=request.POST['au']
        WO=Webpage.objects.get(pk=pk)
        AO=AccessRecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
        AO.save()
        QSAO = AccessRecord.objects.all()
        d1 = {'QSAO':QSAO}
        print(d1)
        return render(request,'display_access.html',d1)
    return render(request,'insert_access.html',d)

def select_and_display(request):
    LTO = Topic.objects.all()
    d = {'LTO':LTO}
    if request.method=='POST':
        tnlist=request.POST.getlist('tn')

        QSWO=Webpage.objects.none()
        for tn in tnlist:
            QSWO=QSWO|Webpage.objects.filter(topic_name=tn)
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_and_display.html',d)

def checkbox(request):
    LTO = Topic.objects.all()
    d = {'LTO':LTO}
    return render(request,'checkbox.html',d)


def radio(request):
    LTO = Topic.objects.all()
    d = {'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        QSWO=Webpage.objects.all()

        QSWO=Webpage.objects.filter(topic_name=tn).delete()
        QSWO=Webpage.objects.all()

        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'radio.html',d)