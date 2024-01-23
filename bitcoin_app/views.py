from django.shortcuts import render, redirect
from django.contrib.auth.models import  auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
from .models import Portfolio, Transactions


# Create your views here.


def home(request):

    
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username = username, password= password)

            if user is not None:
                auth.login(request,user)
                return redirect('portfolio')
            else:
                messages.info(request, 'Contact us on our social accounts below')
                return redirect('signin')

    
    return render(request, 'signin.html')


def register(request):
    form_name = UserForm()
    if request.method =="POST":
        form_name = UserForm(request.POST)
        if form_name.is_valid():
            form_name.save()
            messages.success(request, "You have registered successfully")
            return redirect('signin')
        else:
            messages.error(request, 'Password not secure') 
            return redirect('register')
    else:
        context = {'form_name':form_name}
        
    return render(request, 'register.html', context )


@login_required
def portfolio(request):
    log_user = request.user

    # Check if the user is authenticated before filtering the Portfolio model
    if log_user.is_authenticated:
        portfolio = Portfolio.objects.filter(username=log_user)
    else:
        # If the user is not authenticated, set portfolio to None
        portfolio = None
    
    return render(request, 'portfolio.html', {'portfolio': portfolio})


@login_required
def buy_crypto(request):
    log_user = request.user

    # Check if the user is authenticated before filtering the Portfolio model
    

    
    return render(request, 'buy-sell-crypto.html',)

@login_required
def how_it_works(request):
    
    return render(request, 'how_it_works.html')

@login_required
def support(request):
    
    return render(request, 'support.html')

@login_required
def withdraw(request):
    
    return render(request, 'withdraw.html')


def logout(request):
    auth.logout(request)
    return redirect('signin')