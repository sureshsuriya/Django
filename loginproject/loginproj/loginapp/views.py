from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import logdb
import re
# Create your views here.
def login(request):
    s=''
    f=False
    if 'bu' in request.POST:
        nam=request.POST['name']
        pasw=request.POST['pass'].encode()
        grnd=request.POST['gender']
        cours=request.POST['course']
        phone=request.POST['num']
        imag=request.POST['img']
        if nam!='' and pasw!='' and grnd!='' and cours!='' and phone!='' and re.match('^(\d{10})$',phone):
            x = logdb.objects.filter(num =phone).exists()
            if not x:
               s=logdb(name=nam,passw=pasw,gend=grnd,cou=cours,num=phone,img=imag)
               s.save()
               s = ''
    elif 'bu1' in request.POST:
        s=logdb.objects.all()
    elif 'bu2' in request.POST:
        s=logdb.objects.all()
        for i in s:
            i.delete()
    elif 'bu3' in request.POST:
        nam=request.POST['name']
        f = True
        s = logdb.objects.filter(name = nam).get()
    elif 'bu4' in request.POST:
        nam=request.POST['name']
        pasw=request.POST['pass'].encode()
        grnd=request.POST['gender']
        cours=request.POST['course']
        phone=request.POST['num']
        imag=request.POST['img']
        f = True
        s = logdb.objects.filter(name= nam).get()
        s.passw=pasw
        s.gend = grnd
        s.cou = cours
        s.num = phone
        s.save()
    elif 'bu5' in request.POST:
        nam=request.POST['name']
        s = logdb.objects.filter(name = nam).get()
        s.delete()
    elif 'bu6' in request.POST:
       return redirect(log1)
    return render(request,'login.html',{'obj':s,'f':f})
def log1(request):
    f = False
    s = ''
    if 'log' in request.POST:
        nam=request.POST['name']
        pasw=request.POST['pass'].encode()
        s = logdb.objects.filter(name = nam,passw=pasw).exists()
        if s:
            s = logdb.objects.filter(name = nam,passw=pasw).get()
            f = True
            return redirect('loginapp:log2', f = s)
        else:
            f = 'invalid'
    return render(request,'login1.html',{'obj':s,'f':f})
def log2(request,f):
    if 'le' in request.POST:
        return log3(request,f)
    return render(request,'login2.html',{'obj':f})
def log3(request,s):
    f = True
    if 'sub' in request.POST:
        nam=request.POST['name']
        pasw=request.POST['pass'].encode()
        grnd=request.POST['gender']
        cours=request.POST['course']
        phone=request.POST['num']
        imag=request.POST['img']
        f = True
        s = logdb.objects.filter(name= nam).get()
        s.passw=pasw
        s.gend = grnd
        s.cou = cours
        s.num = phone
        s.save()
    return render(request,'login3.html',{'obj':s,'f':f})