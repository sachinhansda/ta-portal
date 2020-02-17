# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    	BaseUserManager, 
	AbstractUser
)

# Create your models here.
class User(AbstractUser):
	USER_TYPES = (
		(2,'assistant'),
		(1,'teacher'),
		(0,'admin'),
	)
	
	User = get_user_model()
	user_type = models.IntegerField(choices=USER_TYPES)

class Assistant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=10)


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=10)

class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=10)

class Course(models.Model):
	COURSE_TYPES = (
		('L','Lab'),
		('T','Theory'),
	)
	course_id = models.CharField(max_length=20)
	name = models.CharField(max_length=255)
	department = models.CharField(max_length=100)
	credits = models.IntegerField()
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	course_type = models.CharField(max_length=1, choices=COURSE_TYPES)

class Assisting(models.Model):
	assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Declaration(models.Model):
	MONTHS = (
		('Jan','January'),
		('Feb','February'),
		('Mar','March'),
		('Apr','April'),
		('May','May'),
		('Jun','June'),
		('Jul','July'),
		('Aug','August'),
		('Sep','September'),
		('Oct','October'),
		('Nov','November'),
		('Dec','December'),
	)
	APPROVALS = (
		('Y','Yes'),
		('N','No'),
	)
	month = models.CharField(max_length=3, choices=MONTHS)
	avg_hours = models.IntegerField()
	days = models.IntegerField()
	approval = models.CharField(max_length=1, choices=APPROVALS)
	rating = models.DecimalField(max_digits=3, decimal_places=2)

class assistant_preference(models.Model):
	assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, default="", editable=False)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, default="")
	preference = models.IntegerField()

class teacher_preference(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
	preference = models.IntegerField()
