from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def allregister(request):
    d={'TO':Topicforms(),'WO':Webpageforms(),'AO':Accessrecordforms()}
    if request.method=='POST':
        dTO=Topicforms(request.POST)
        DWO=Webpageforms(request.POST)
        DAO=Accessrecordforms(request.POST)
        if dTO.is_valid() and DWO.is_valid() and DAO.is_valid():
            tnso=dTO.save(commit=False)
            tnso.save()
            NSW=DWO.save(commit=False)
            NSW.topic_name=tnso
            NSW.save()
            dnso=DAO.save(commit=False)
            dnso.name=NSW
            dnso.save()
            return HttpResponse('register is done..!')
        else:
            return  HttpResponse('invalid data')

    return render(request,'allregister.html',d)