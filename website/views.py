from unicodedata import *
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from django.shortcuts import  redirect, render
from .models import *
from .forms import *
from django.db.models import *
from django.contrib.auth.models import Group
from django.contrib.auth import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def profile(request):
    return render(request, 'profile.html')


def registeratsiya(request):
    return render(request, 'registeratsiya.html')
        
     

def Aboutus_View(request):
    
    return render(request,'main/aboutus.html')

def Contacts_View(request):
    
    return render(request,'main/contacts.html')

def News_View(request):
    
    return render(request,'main/news.html')

def Detailed_News(request):

    return render(request,'main/detailednew.html')

def Portfolio(request):

    return render(request,'main/portfolio.html')

def Services_View(request):
    main = Service.objects.all()
    context = {"service": main}
    return render(request,'main/services.html', context=context)


# Yangi qo'shilgan narsalar!
class NewListView(ListView):
    queryset = New.objects.all()
    # print(New.objects.all()) tekshirish!!!
    template_name = 'main/news.html'   
    context_object_name = 'New'


class NewDetailView(DetailView):
    template_name = 'main/detailednew.html'
    model = New


class OrganizationListView(ListView):
    queryset = Organization.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'Organization'


class OrgnizationDetailView(DetailView):
    template_name = 'main/about_me.html'
    model = Organization




def user_login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, template_name='user-login.html', context={'form': form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user:
                login(request=request, user=user)
                return redirect('service')
            else:
                return render(request, template_name='user-login.html', context={'form': form})


def user_register_view(request):
    if request.method == 'GET':
        form = UserRegisterModelForm()
        return render(request, template_name='user-register.html', context={'form': form})
    else:
        form = UserRegisterModelForm(data=request.POST)
        password = request.POST['password']
        confirm = request.POST['confirm']
        if form.is_valid() and password == confirm:
            form.save()
            user = form.instance
            user.groups.add(Group.objects.get(name='Xaridor'))
            user.save()

            login(request, user)

            return redirect('service')
        else:
            return render(request, template_name='user-register.html', context={'form': form})





