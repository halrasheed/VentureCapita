from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Project, Shares
from datetime import date


#################################################################
def indexfunction(request : HttpRequest):
    projects = Project.objects.all()
    context = {"projects" : projects}
    return render(request, "main/index.html", context)
#################################################################
def userRegisterFun(request : HttpRequest): 
   if request.method == "POST": 
        newUser = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"]) 
        newUser.save() 
        return redirect("main:login")
   return render(request, "main/register.html")
#################################################################
def userAuthFun(request : HttpRequest): 
    msg = None
    if request.method == "POST": 
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"] ) 
            if user is not None:
                login(request, user)
                return redirect("main:index")
            else:
                msg = "Try again"
    return render (request,"main/login.html", {"msg":msg} )        
#################################################################
def userLogoutFun(request : HttpRequest):
    logout(request)
    return redirect("main:index")
#################################################################
def newProjectFun(request :HttpRequest): 
    if not request.user.is_staff: 
        return redirect("main:login") 
    if request.method == "POST": 
        newProject = Project(name= request.POST["name"], feature_image = request.FILES["feature_image"], description = request.POST["description"], department=request.POST["department"], risk=request.POST["risk"], expected_Return=request.POST["expected_Return"], established_at=request.POST["established_at"]) 
        newProject.save() 
        return redirect("main:index") 
    return render(request, "main/newProject.html")
#################################################################
def projectDetailsFun(request : HttpRequest, project_id): 
    project = Project.objects.get(id=project_id) 
    appointments = Shares.objects.filter(project=project)
    if request.user.is_authenticated :
        usrShares = Shares.filter(user = request.user)
        return render(request, "main/projectDetails.html", {"project" : project, "usrShares" : usrShares})
    return render(request, "main/projectDetails.html", {"project" : project}) 
#################################################################
def findProjectFun(request : HttpRequest):
    if request.method == "POST":
        toFind = request.POST['toFind']  
        result = Project.objects.filter(name__contains=request.POST['toFind'] )
        return render(request, "main/findProject.html", {'toFind' : toFind , 'result' : result})
    else:
        return render(request, "main/findProject.html", {'toFind' : toFind})
#################################################################
