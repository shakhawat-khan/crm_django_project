# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import * # here we import customer form the customer model because now we can create table on admin site

admin.site.register(customer) # now we see the class in the admin django site

admin.site.register(order)

admin.site.register(product)

admin.site.register(tag)
