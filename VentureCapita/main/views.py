from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Project, Users, Shares
from datetime import date


#################################################################
def indexfunction(request : HttpRequest):
    ''' Index Function '''
    projects = Project.objects.all()
    context = {"projects" : projects}
    return render(request, "main/index.html", context)
#################################################################
def userRegisterFunction(request : HttpRequest): 
   ''' Function  for registering new users '''
   if request.method == "POST": 
        newUser = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
        newUser.save()
        addBalance = Users(user= newUser, balance = 100) 
        addBalance.save()
        return redirect("main:profile")
   return render(request, "main/register.html")
#################################################################
def userAuthFunction(request : HttpRequest): 
    '''  Function for Authintcate Users '''
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
def userLogoutFunction(request : HttpRequest):
    '''  Function for for logout user '''
    logout(request)
    return redirect("main:index")
#################################################################
def newProjectFunction(request :HttpRequest): 
    '''  Function for creating New user '''
    if not request.user.is_staff: 
        return redirect("main:login") 
    if request.method == "POST": 
        newProject = Project(name= request.POST["name"], feature_image = request.FILES["feature_image"], description = request.POST["description"], department=request.POST["department"], risk=request.POST["risk"], expected_Return=request.POST["expected_Return"], established_at=request.POST["established_at"], sharesCount=request.POST["sharesCount"], sharesValue=request.POST["sharesValue"], sharesAvailable = request.POST["sharesCount"]) 
        newProject.save() 
        return redirect("main:index") 
    return render(request, "main/newProject.html")
#################################################################
def projectDetailsFunction(request : HttpRequest, project_id): 
    '''  Function for browsing and selling project shares '''
    project = Project.objects.get(id=project_id) 
    shares = Shares.objects.filter(project=project)
    if request.user.is_authenticated :
        usrShares = shares.filter(user = request.user)
        return render(request, "main/projectDetails.html", {"project" : project, "usrShares": usrShares})
    return render(request, "main/projectDetails.html", {"project" : project}) 
#################################################################
def findProjectFunction(request : HttpRequest):
    '''  Function for searching for a project '''
    if request.method == "POST":
        toFind = request.POST['toFind']  
        result = Project.objects.filter(name__contains=request.POST['toFind'] )
        return render(request, "main/findProject.html", {'toFind' : toFind , 'result' : result})
    else:
        return render(request, "main/findProject.html", {'toFind' : toFind})
#################################################################
def updateProjectFunction(request : HttpRequest):
    '''  Function for for updating a project '''
    projects = Project.objects.all()
    context = {"projects" : projects}
    return render(request, "main/index.html", context)
#################################################################
def buyBeforFunction (request : HttpRequest, project_id):
    '''  Function for buying shares '''
    buy_msg=None
    project = Project.objects.get(id=project_id) 
    user : Users=request.user
    shares = Shares.objects.get(id=project_id)
    wantedCount= request.POST['wantedCount']
    sharesPraice = wantedCount*project.sharesValue
    if (user.balance >= sharesPraice and wantedCount <= project.sharesAvailable):
        user.balance = user.balance - sharesPraice
        shares.user = shares.user + wantedCount
        project.sharesAvailable = project.sharesAvailable - wantedCount
        shares.save()
        project.save()
        return render(request, "main/profile.html")
    else:
        buy_msg = "You Cannot Buy This Shares"
        return render(request, "main/findProject.html", {'buy_msg' : buy_msg})
##################################################################
def profileFunction(request : HttpRequest, user_id):
    '''  Function for browsing user dashbord '''
    user : Users=request.user
    shares = Shares.objects.filter(user=user)
    #projectName = shares.project
    context = {"user":user, "shares":shares}
    return render(request, "main/profile.html", context)
##################################################################

##################################################################

##################################################################
    
