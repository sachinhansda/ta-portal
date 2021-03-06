# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
#from accounts.forms import EditProfileForm, ProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
def view_profile(request):
	user = request.user
	args = {'user': user}
	return render(request, 'accounts/profile.html', args)


def edit_profile(request):
	if request.method  == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)

		if form.is_valid() and profile_form.is_valid():
			user_form = form.save()
			custom_form = profile_form.save(False)
            		custom_form.user = user_form
            		custom_form.save()
			return redirect('/accounts/profile')

	else:
		form = EditProfileForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
		args = {'form': form, 'profile_form': profile_form}
		return render(request, 'accounts/edit_profile.html', args)

def add(request):
	args = {}
	return render(request, 'accounts/add.html', args)

def profile(request):
	args = {}
	return render(request, 'accounts/profile_view.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')
	else:
		form = PasswordChangeForm(user=request.user)

		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)
"""
