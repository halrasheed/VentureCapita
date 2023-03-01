from django.contrib import admin
from .models import Project, Shares

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','department')



#class SharesAdmin(admin.ModelAdmin):
    #list_display = ()



admin.site.register(Project,ProjectAdmin)

#admin.site.register(Shares,Shares)
# Register your models here.
