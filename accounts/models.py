# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200 , null = True)
    phone = models.CharField(max_length=200 , null = True )
    email = models.CharField(max_length=200 , null = True)
    profile_pic = models.ImageField(null=True,blank=True, default='default.jpg' )
    date_created = models.DateField(auto_now_add = True)

    def __str__(self):   
        return self.name  


class product(models.Model):

    CATEGORY = (
        ('Indoor' , 'Indoor' ),
        ('Out Door' ,'Out Door' ),

    )

    name = models.CharField(max_length=200 , null = True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200 , null = True , choices= CATEGORY)
    description = models.CharField(max_length=200 , null = True)
    date_created = models.DateField(auto_now_add = True)

    def __str__(self):   
        return self.name  



class tag(models.Model):
    name = models.CharField(max_length=200 , null = True)

    def __str__(self):   
        return self.name  



class order(models.Model):
    
    STATUS = (

        ('pending' , 'Pending' ),
        ('Out for delivery' ,'out for delivery' ),
        ('Deliverd' , 'Deliverd'),



    )
    
    customer = models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(product,null=True,on_delete = models.SET_NULL)

    date_created = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=200 , null = True ,choices=STATUS) 
    tag = models.ManyToManyField(tag)

    note = models.CharField(max_length=200 , null = True)
    
    def __str__(self):   
        return self.product.name  

    