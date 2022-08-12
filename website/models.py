from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Organization(models.Model):
    name=models.CharField(max_length=170)
    logo=models.ImageField(blank=True, null=True)
    info=RichTextField()
    instagram=models.CharField(max_length=255,blank=True,null=True)
    youtube=models.CharField(max_length=255,blank=True,null=True)
    telegram=models.CharField(max_length=255,blank=True,null=True)
    tel=models.CharField(max_length=13)
    tel2=models.CharField(max_length=13)
    tel3=models.CharField(max_length=13)
    mail=models.EmailField(max_length=50)
    address=models.CharField(max_length=170)


class New(models.Model):
    header=models.CharField(max_length=250)
    image=models.ImageField(blank=True, null=True)
    info=RichTextField()
    status_name=[
         (True, 'Active'),
        (False, 'Inactive'),
    ]
    status = models.BooleanField(choices=status_name, default=True, blank=True)

class ServiceType(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return f"{self.name}"

class Service(models.Model):
    name=models.CharField(max_length=250)
    info=RichTextField()
    type = models.ForeignKey(ServiceType(), on_delete=models.CASCADE)
    status_name=[
         (True, 'Active'),
        (False, 'Inactive'),
    ]
    status = models.BooleanField(choices=status_name, default=True, blank=True)
class Partners(models.Model):
    name=models.CharField(max_length=250)
    logo=models.ImageField(blank=True, null=True)

class Region(models.Model):
    name=models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "7.Viloyat"
class District(models.Model):
    name=models.CharField(max_length=250)
    region=models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        verbose_name_plural = "6.Turmanlar"
class Customer(models.Model):
    name=models.CharField(max_length=250)
    inn=models.CharField(max_length=7,unique=True)
    tel=models.CharField(max_length=30,null=True,blank=True)
    login=models.CharField(max_length=250,null=True,blank=True)
    passwrod=models.CharField(max_length=250,null=True,blank=True)
    status_name=[
        (True,'Faol'),
        (False,'Faol emas'),
    ]
    status=models.BooleanField(choices=status_name,default=False)
    region=models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    who_send_name=[
        (True,'O`zi aloqaga chiqan'),
        (False,'Tashqi tashkilot orqali')
    ]
    who_send=models.BooleanField(choices=who_send_name, default=True)
    firma_name_sender=models.CharField(max_length=250,null=True,blank=True)
    class Meta:
        verbose_name_plural = "2.Mijozlar"
    def __str__(self):
        # Return a string that represents the instance
        return f"{self.id}::{self.name}"

class Substation(models.Model):
    name=models.CharField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name_plural = "5.Nimstansiya"
class Meter_type(models.Model):
    name=models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "4.Hisoblagich turi"
class Fider(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE, null=True, blank=True)
    number=models.PositiveIntegerField(blank=True,null=True)
    trant_tok=models.CharField(max_length=100,null=True,blank=True)
    trant_n=models.CharField(max_length=100,null=True,blank=True)
    meter_type=models.ForeignKey(Meter_type,on_delete=models.CASCADE,null=True,blank=True)
    status_name = [
        (True, 'Faol'),
        (False, 'Faol emas'),
    ]
    status = models.BooleanField(choices=status_name, default=False)
    class Meta:
        verbose_name_plural = "3.Fiderlar"
class Agreement(models.Model):
    name=models.CharField(max_length=70)
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    price=models.FloatField(null=True,blank=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    agree_name=[
        (1,'Yuborilgan'),
        (2,'Tasdiqlangan'),
        (3,'Tugagan')
    ]
    agree_status=models.PositiveIntegerField(choices=agree_name,default=1)
    hisob_name=[
        (True,'Hisob faktura yuborilmagan!'),
        (False, 'Hisob faktura yuborilgan***'),
    ]
    hisob=models.BooleanField(choices=hisob_name,default=True)
    status_name = [
        (True, 'Faol'),
        (False, 'Faol emas'),
    ]
    status = models.BooleanField(choices=status_name, default=False)
    class Meta:
        verbose_name_plural = "1.Shartnomalar"

class Conn_agre(models.Model):
    agreement=models.ForeignKey(Agreement,on_delete=models.CASCADE,null=True,blank=True)
    fider=models.ForeignKey(Fider,on_delete=models.CASCADE,null=True,blank=True)