# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Shop(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True)
	adress = models.CharField(max_length=30, blank=True, null=True)
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	
	def __str__(self):
		return self.adress

class Artwork(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True)
	shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
	price = models.IntegerField(blank=True, null=True)
	artist = models.CharField(max_length=20, blank=True, null=True)
	product_num = models.CharField(max_length=45, blank=True, null=True)
	

	def __str__(self):
		return self.product_num

class product(models.Model):
	proname = models.CharField(max_length=20, blank=True, null=True)
	proprice = models.IntegerField(blank=True, null=True)
	procont = models.CharField(max_length=255,blank=True, null=True)
	pronum = models.IntegerField(blank=True, null=True)
	proimg = models.CharField(max_length=255,blank=True, null=True)
	procate = models.CharField(max_length=20, blank=True, null=True)
	proid = models.CharField(primary_key=True,max_length=45, blank=True)
	def __str__(self):
		return self.proname

class cate(models.Model):
	cateid = models.AutoField(primary_key=True)
	catename = models.CharField(max_length=10, blank=True, null=True)
	def __str__(self):
		return self.catename