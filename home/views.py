from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import *
from .forms import PpicForm,BpicForm



def home(request):
    return render(request, 'Home.html')

def Login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request , user)
            print('Logged in')
            return redirect('User')
        else:

            messages.error(request,'Invalid credentials, try again')
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')

    
def mbplan(request):
    return render(request, 'mbplan.html')


def User(request):
   return render(request, 'User.html')

def faq(request):
    return render(request, 'faq.html')


def pupload(request):
    info=request.user.profile
    i_form = PpicForm(instance=info)
    if request.method =='POST':
        i_form = PpicForm(request.POST, request.FILES,instance=info)
        if i_form.is_valid():
            i_form.save()
            context = {'form' : i_form}
            return render(request, 'Pupload.html',context)

    else:
        print("non-post")
        return render(request, 'Pupload.html')




def bond(request):
    info=request.user.profile
    b_form = BpicForm(instance=info)
    if request.method =='POST':
        b_form = BpicForm(request.POST, request.FILES,instance=info)
        if b_form.is_valid():
            b_form.save()
            context = {'form' : b_form}
            return render(request, 'bondpic.html',context)


    else:
        print("non-post")
        return render(request, 'bondpic.html')
   



def Logout(request):
    auth.logout(request)
    return redirect('/')





def Child(request):
    return render(request, 'plan/Child.html')

def Endowment(request):
    return render(request, 'plan/endplans.html')

def Health(request):
    return render(request, 'plan/Health.html')

def MoneyBack(request):
    return render(request, 'plan/MoneyBack.html')

def Pension(request):
    return render(request, 'plan/Pension.html')
