from django.db import models
from django.conf import settings

# Create your models here.
sex= {
    ("M", "Male"),
    ("F", "Female"),

}

class FormModel(models.Model):
    user= models.CharField(max_length=200, )
    first_name =models.CharField(max_length=200, )
    middle_name =models.CharField(max_length=200, )
    last_name= models.CharField(max_length=200, )
    Id_number=models.CharField(max_length=200, )
    dob = models.DateField()
    gender =models.CharField(choices=sex, max_length=5)
    fixed = models.CharField(max_length=200, null=True, blank=True)
    dob_id_section =models.CharField(max_length=40, null=True, blank=True)
    name_section =models.CharField(max_length=40,null=True, blank=True )

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True, blank=True)
    phon_number =models.CharField(max_length=40,null=True, blank=True )
    email = models.EmailField(null=True, blank=True,)
    date  = models.DateField(auto_now_add=True,null=True, blank=True)
    amountD= models.IntegerField(default=0.0,null=True, blank=True)
    amountS = models.IntegerField(default=0.0,null=True, blank=True)
    amountB = models.IntegerField(default=0.0, null=True, blank=True)


class CsvFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True, blank=True)
    csv_file = models.FileField(upload_to='documents')
