# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.db import models
from django.contrib.auth.models import (
    	BaseUserManager, 
	AbstractUser
)

# Create your models here.
class User(AbstractUser):
	USER_TYPES = (
		('assistant'),
		('teacher'),
		('admin'),
	)
	
	user_type = models.CharField(choices=USER_TYPES)

class Assistant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=10)


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=10)

class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=10)

class Course(models.Model):
	COURSE_TYPES = (
		'Lab',
		'Theory',
	)
	course_id = models.CharField(max_length=20)
	name = models.CharField(max_length=255)
	department = models.CharField(max_length=100)
	credits = models.IntegerField()
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, primary_key=True)
	course_type = models.CharField(max_length=10, choices=COURSE_TYPES)

class Assisting(models.Model):
	assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, primary_key=True)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, primary_key=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, primary_key=True)

class Declaration(models.Model):
	MONTHS = (
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December',
	)
	APPROVALS = (
		'Yes',
		'No',
	)
	month = models.CharField(max_length=15, choices=MONTHS)
	avg_hours = models.IntegerField()
	days = models.IntegerField()
	approval = models.CharField(max_length=3, choices=APPROVALS)
	rating = models.DecimalField()

class assistant_preference(models.Model):
	assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, primary_key=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, primary_key=True)
	preference = models.IntegerField()

class assistant_preference(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, primary_key=True)
	assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, primary_key=True)
	preference = models.IntegerField()
