# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models

class Cate(models.Model):
	cateid = models.AutoField(primary_key=True)
	catename = models.CharField(max_length=20, blank=True, null=True)
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.catename

class Product(models.Model):
	proname = models.CharField(max_length=20, blank=True, null=True)
	proprice = models.IntegerField(blank=True, null=True)
	procont = models.CharField(max_length=255,blank=True, null=True)
	pronum = models.IntegerField(blank=True, null=True)
	proimg = models.CharField(max_length=255,blank=True, null=True)
	procate = models.ForeignKey(Cate,on_delete=models.CASCADE)
	proid = models.CharField(primary_key=True,max_length=45, blank=True)
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.proname

class ShoppingCart(models.Model):
	memberid = models.CharField(primary_key=True,max_length=45, blank=True)
	selectproduct = models.ForeignKey(Product,on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.memberid

class SuccessOrder(models.Model):
	orderid = models.AutoField(primary_key=True)
	memberid = models.CharField(max_length=45, blank=True)
	selectproduct = models.ForeignKey(Product,on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.memberid

class LeaveMessage(models.Model):
	orderid = models.ForeignKey(SuccessOrder,on_delete=models.CASCADE)
	memberid = models.CharField(primary_key=True,max_length=45, blank=True)
	selectproduct = models.ForeignKey(Product,on_delete=models.CASCADE)
	contant = models.TextField()
	ifbuy = models.BooleanField()
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.memberid

class Member(models.Model):
	memberid = models.AutoField(primary_key=True)
	memberaccount = models.CharField(max_length=40,blank=True, null=True)
	memberpas = models.CharField(max_length=40,blank=True, null=True)
	membername = models.CharField(max_length=20, blank=True, null=True)
	memberphone = models.IntegerField(blank=True, null=True)
	memberaddres = models.CharField(max_length=255,blank=True, null=True)
	memberkey = models.CharField(max_length=10,blank=True, null=True)
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.memberid