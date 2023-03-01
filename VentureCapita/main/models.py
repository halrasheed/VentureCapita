from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project (models.Model):

    name                = models.CharField(max_length=200)
    feature_image       = models.ImageField(upload_to="images/", default="images/default.jpg")
    description         = models.TextField()

    department_choises  = models.TextChoices("department", ['Construction', 'RealEstate', 'Health Care', 'Import/Export', 'Technology', 'Utility', 'Other'])
    department          = models.CharField(max_length=200, choices= department_choises.choices)

    risk_Eval_choises         = models.TextChoices("risk", ['High', 'Medium', 'Low', 'Unknown'])
    risk = models.CharField(max_length=200, choices= risk_Eval_choises.choices)

    expected_Return_choises         = models.TextChoices("expected_Return", ['10%<##>30%', '30%<##>50%', '50%<##>70%', '70%<##', 'Other'])
    expected_Return = models.CharField(max_length=200, choices= expected_Return_choises.choices)

    established_at      = models.DateTimeField(auto_now_add=True)
    sharesCount         = models.PositiveIntegerField()
    sharesValue         = models.PositiveIntegerField()
    sharesAvailable     = models.PositiveIntegerField()
    def __str__(self) -> str:
        return f"{self.name}"
###################################################
class Users (models.Model):

    user                 = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    balance              = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.user.first_name}"
###################################################
class Shares (models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete= models.CASCADE)
    shares  = models.IntegerField ()



