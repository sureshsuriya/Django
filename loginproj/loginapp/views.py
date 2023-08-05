from django.shortcuts import render
from django.http import HttpResponse
from .models import StdDb
# Create your views here.
def log(request):
    l={'suresh':'123','ram':'456','kumar':'789'}
    s1 = ''
    if 'but' in request.POST:
        r=request.POST['name']
        s=request.POST['pass']
        if r!='' and s!='':
            if r in l and l[r] == s:
                s1 = StdDb(sname = r,pwd = s)
                s1.save()
                #  return log2(request)
    elif 'but2' in request.POST:
        s1 = StdDb.objects.all()
    return render (request,'login.html',{'obj':s1})
def log2(request):
    return render (request,'login1.html')