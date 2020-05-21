from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.
class profile(models.Model):
    user= models.OneToOneField(to=User, on_delete=CASCADE)
    pname=models.CharField(max_length=100)
    nname=models.CharField(max_length=100)
    nrel=models.CharField(max_length=100)
    pstatus=models.CharField(max_length=100)
    plan=models.CharField(max_length=100)
    plantype=models.CharField(max_length=100)
    mode=models.CharField(max_length=100)
    nshare=models.IntegerField()

    polnum=models.IntegerField()
    polterm=models.IntegerField()
    prempayterm=models.IntegerField()
    sum=models.IntegerField()

    ptotal=models.IntegerField()
    svalue=models.IntegerField()
    mvalue=models.IntegerField()
    mbonus=models.IntegerField()
    loanavl = models.BooleanField()
    maxloan=models.IntegerField()

    npreceipt = models.FileField(upload_to='recipts/')
    revival = models.FileField(null=True, blank=True, upload_to='revival/')
    details = models.FileField(null=True, blank=True, upload_to='details/')
    revival = models.BooleanField(default="True")
    bond_given = models.BooleanField(default="True")

    age=models.IntegerField()
    dob=models.DateField(blank="ture")
    doc=models.DateField(blank="ture")
    dom=models.DateField(blank="ture")
    dop=models.DateField(blank="ture")
    npamount=models.IntegerField()
    npamountwt=models.IntegerField()



    ppic=models.ImageField(default='default.jpg' , upload_to='profile_pics')
    bpic=models.ImageField(default='default1.jpg' , upload_to='bond_pics')
    adrfpic=models.ImageField(default='defaultaf.jpg' , upload_to='adr_pics')
    adrbic=models.ImageField(default='defaultab.jpg' , upload_to='adr_pics')

    def __str__(self):
        return self.pname
