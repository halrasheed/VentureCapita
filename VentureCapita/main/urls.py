from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",                         views.indexfunction,        name="index"),
    path("register",                 views.userRegisterFunction,      name="register"),
    path("login",                    views.userAuthFunction,          name="login"),
    path("logout/",                  views.userLogoutFunction,        name="logout"),
    path("add/",                     views.newProjectFunction,        name="newProject"),
    path("details/<project_id>/",    views.projectDetailsFunction,    name="projectDetails"),
    #path("update/<project_id>/",    views.updateProjectFunction,     name="updateProjct"),
    path("find/",                    views.findProjectFunction,       name="findProject" ),
    path("profile/",                 views.profileFunction,           name="profile" ),
    path("buy/<project_id>/",        views.buyBeforFunction,          name="buy" ),
]##