from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# Sample dictionary of username and password (for demonstration purposes)
user_credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
    # Add more username and password pairs if needed
}

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username in user_credentials and user_credentials[username] == password:
            return render(request, 'welcome.html', {'username': username})
        else:
            # Invalid credentials, show an error message or redirect to the login page
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
def mod(request):
    if 'but' is request.POST:
        l={'suresh':"123",'ram':'456','kumar':'789'}
        s=request.POST['name']
        r=request.POST['pass']
        if s!='' and r!='' :
            if s in l:
                if l[s]==int(r):
                    return mod2(request,s,r)
    return render(request,'moduel.html')
def mod2(request,x,y):
    k={'nam':x,'pa':y}
    return render(request,'moduel2.html',k)
