from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",                         views.indexfunction,        name="index"),
    path("register",                 views.userRegisterFun,      name="register"),
    path("login",                    views.userAuthFun,          name="login"),
    path("logout/",                  views.userLogoutFun,        name="logout"),
    path("add/",                     views.newProjectFun,         name="newProject"),
    path("details/<clinic_id>/",     views.projectDetailsFun,     name="projectDetails"),
    #path("update/<clinic_id>/",      views.updateClinicFun,      name="updateClinic"),
    path("find/",                    views.findProjectFun,        name="findProject" ),
    #path("addA/<clinic_id>/",        views.newAppointmentFun,    name="addAppointment"),
    
]##