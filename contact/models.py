# -*- coding: utf-8 -*-
"""
@author: dan.wlodarski
"""
from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    base_zipcode = models.CharField('USPS ZIP Code', max_length=5)
    plus4_zipcode = models.CharField('USPS ZIP+4', max_length=4, blank=True, null=True)
    comment = models.TextField()

    def __str__(self):
        return "%s <%s>" % (self.name, self.email)

    def get_absolute_url(self):
        return reverse('')
