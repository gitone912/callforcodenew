from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from .models import feedback, homepage,Video
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import NewUserForm
from django.views.decorators.clickjacking import xframe_options_exempt
from .form import VideoForm


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('profile')
        else:
            messages.info(request,"Invalid username or password.")
    return render(request ,'app/login.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="app/register.html", context={"form":form})

def logoutpage(request):
    logout(request)
    return redirect('home')
        
def HomePage(request):
    a_homepage=homepage.objects.all()
    video = Video.objects.all()
    if request.method == 'POST':
        contact=feedback()
        feedbck=request.POST.get('feedbck')
        contact.feedbck=feedbck
        contact.save()
        return render(request,'app/thanks.html')
    context={'homepage':a_homepage,'video':video}
    return render(request,'app/index.html',context)

@login_required
def userprofile(request):
    return render(request,'app/welcome.html')

def showvideo(request):  # sourcery skip: aug-assign
    a=0
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        a=a+1
        
    context= {
        # 'videofile': videofile,
              'form': form,
              "points":a
              }
    
    return render(request, 'app/blogs.html', context)

def rendervideo(request):
    video= Video.objects.all()
    return render(request,'app/list.html',{'videofile' : video})
