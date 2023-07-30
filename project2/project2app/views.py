from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    # l=['suresh',123,'ram',456,'kumar',789]
    l={'suresh':"123",'ram':'456','kumar':'789'}
    if 'sub' in request.POST:
        s=request.POST['name']
        r=request.POST['pass']
        if s!='' and r!='' :
            if s in l:
                if l[s]==r:
                    return log2(request,s,r)
    return render(request,'moduel.html')
def log2(request,s,r):
    f={'name':s,'pa':r}
    return render(request,'moduel2.html',f)
def hom(request):
    if 'sub' in request.POST:
         z=request.POST['Uname']
         r=request.POST['Pass']
         c=request.POST['email']
         v=request.POST['age']
         b=request.POST['gender']
         if z!='' and r!='' and c!='' and v!='' and b!='':
            return hom2(request,z,r,c,v,b)
    return render (request,"home.html")
def hom2(requset,z,r,c,v,b):
    inf={'nam':z,'pass':r ,'gma':c,'ag':v,'ged':b}
    return render (requset,'home2.html',inf)
def ad(request):
    if 'ADD' in request.POST:
         w=request.POST['num1']
         s=request.POST['num2']
         if w!='' and s!='':
            try:
                w = int(w)
                s = int(s)
                x = w+s
            except:
                x = w+s
            return test(request,x)
    return render(request,'test.html')
def test(request,a):
    ans = {'ans':a}
    return render (request,'test2.html',ans)     
def age(request):
    if 'sub' in request.POST:
        Q=request.POST['age']
        if int(Q)<=18:
            return subm(request,Q)
        elif int(Q)>18:
            return subm1(request,Q)
    return render (request,'age.html')
def subm(request,w):
    u={'k':w}
    return render(request,'age1.html',u)
def subm1(request,ag):
    u={'n':ag}
    return render(request,'age2.html',u)