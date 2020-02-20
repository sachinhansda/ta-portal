# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    	STUDENT = 1
    	TEACHER = 2
    	ADMIN = 3
    	ROLE_CHOICES = (
        	(STUDENT, 'Student'),
        	(TEACHER, 'Teacher'),
        	(ADMIN, 'Admin'),
    	)
   	user = models.OneToOneField(User)
    	name = models.CharField(max_length=50, default='')
	department = models.CharField(max_length=30, default='')
    	phone_number = models.CharField(max_length=10)
    	role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

	USERNAME_FIELD = 'user'
	REQUIRED_FIELDS = []
	is_anonymous = False
	is_authenticated = True

    	def __str__(self):  # __unicode__ for Python 2
        	return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    	if created:
        	Profile.objects.create(user=instance)
    	instance.profile.save()

class Course(models.Model):
	COURSE_TYPES = (
		('L','Lab'),
		('T','Theory'),
	)
	course_id = models.CharField(max_length=20)
	name = models.CharField(max_length=255)
	department = models.CharField(max_length=100)
	credits = models.IntegerField()
	students = models.IntegerField(default=0)
	teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
	course_type = models.CharField(max_length=1, choices=COURSE_TYPES)

class Assisting(models.Model):
	assistant = models.ForeignKey(Profile, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Teaching(models.Model):
	teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
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
	assistant = models.ForeignKey(Profile, on_delete=models.CASCADE, default="", editable=False)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, default="")
	preference = models.IntegerField()

class teacher_preference(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE, default="")
	assistant = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
	preference = models.IntegerField()
