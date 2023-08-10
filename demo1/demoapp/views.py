from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import dmdb
import re
# Create your views here.
def log(request):
    if 'bu' in request.POST:
        nam=request.POST['name']
        pasw=request.POST['pass'].encode()
        phone=request.POST['num']
        if nam!='' and pasw!='' and  phone!='' and re.match('^(\d{10})$',phone):
            x = dmdb.objects.filter(num =phone).exists()
            if not x:
               s=dmdb(name=nam,passw=pasw,num=phone)
               s.save()
               s = ''
    elif 'bu6' in request.POST:
       return redirect(log1)
    return render(request,'login.html')
def log1(request):
    if 'log' in request.POST:
        img=request.POST['imge']
        s=dmdb(imge=img)
        s.save()
        
    return render(request,'login1.html')