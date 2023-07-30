from django.shortcuts import render

# import Http Response from django
from django.http import HttpResponse

# Create your views here.
def home1(request):
    return render(request,"home1.html")
def home(request):
    if 'nxt' in request.POST:
        arg = request.POST['inp1']
        wer=request.POST['inp2']
        if arg!='' and wer!='':
            return req(request,arg,wer)
    elif 'prev' in request.POST:
        return fun(request)
    return render(request,"home.html",{'key':3})
def req(request,pk,no):
    return render(request,"req.html",{'name':pk,'roll':no})
def fun(request):
    return render(request,'next.html')
