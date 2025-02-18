from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from Category.models import *
# Create your views here.


def home(request):
    categories = Category.objects.all()
    products=Product.objects.all()
    return render(request, 'base.html', {'categories': categories,'products': products})

@login_required(login_url='login')
def contact(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def product_detail(request,id):
    data = Product.objects.filter(category_id=id)
    return render(request, 'product_detail.html', {'data': data})

@login_required(login_url='login')
def product_info(request,id):
    data = Product.objects.get(id=id)
    return render(request, 'product_info.html', {'data': data})

def Register(request):
    form=RegisterForm()
    if request.method=='POST':
        # user=Account_details.objects.filter(username=request.POST['username'])
        # if user.exists():
        #     messages.info(request,'User Already Exist')
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        # else:
        #     print(form.errors)
            # return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def ulogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Invalid username or password')
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    user=request.user
    data=Account_details.objects.filter(id=user.id)
    return render (request,'profile.html',{'data':data})


@login_required(login_url='login')
def ulogout(request):
    logout(request)
    return redirect('home')


def update(request,id):
    data=Account_details.objects.get(id=id)
    form=UpdateForm(instance=data)
    if request.method == 'POST':
        form=UpdateForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
            return HttpResponse('<h1>Invalid</h1>')
    return render(request,'profile_update.html',{'form':form,'data':data})


