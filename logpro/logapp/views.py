from django.shortcuts import render
from django.http import HttpResponse
from .models import newdb
import re
# Create your views here.
def log(request):
    s=''
    if 'bu' in request.POST:
        w=request.POST['name']
        q=request.POST['pass'].encode()
        d=request.POST['gender']
        y=request.POST['course']
        p=request.POST['num']
        if w !='' and q!=''and d!='' and y!='' and p!='' and re.match('^(\d{10})$',p):#p.isdigit() and len(p) == 10 
            x = newdb.objects.filter(num = p).exists()
            if not x:
               s=newdb(r=w,b=q,g=d,cou=y,num=p)
               s.save()
               s = ''
    elif 'bu1' in request.POST:
        s=newdb.objects.all()
    elif 'bu2' in request.POST:
        s=newdb.objects.all()
        for i in s:
            i.delete()
    elif 'bu3' in request.POST:
        w=request.POST['name']
        s = newdb.objects.filter(r = w).get()
    return render(request,'log.html',{'obj':s})
def imag(request):
     return render(request,'imag1.html')
        
def war(request):
    return render(request,'imag.html')