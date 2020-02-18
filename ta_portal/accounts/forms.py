from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Profile

''' class AssistantRegistrationForm(UserCreationForm):
	name = forms.CharField()
	department = forms.CharField()
	phone_number = forms.CharField()

	class Meta:
		model = User
		fields = (
			'username',
			'name',
			'department',
			'email',
			'phone_number',
			'password1',
			'password2'
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user_type = 'assistant'
		assistant = Assistant.objects.create(user=user)
        	assistant.name = self.cleaned_data['name']
		assistant.department = self.cleaned_data['department']
		assistant.email = self.cleaned_data['email']
		assistant.phone_number = self.cleaned_data['phone_number']

		if commit:
			user.save()

		return user

class TeacherRegistrationForm(UserCreationForm):
	name = forms.CharField()
	department = forms.CharField()
	phone_number = forms.CharField()
	
	class Meta:
		model = User
		fields = (
			'username',
			'name',
			'department',
			'email',
			'phone_number',
			'password1',
			'password2'
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user_type = 'teacher'
		teacher = Teacher.objects.create(user=user)
        	teacher.name = self.cleaned_data['name']
		teacher.department = self.cleaned_data['department']
		teacher.email = self.cleaned_data['email']
		teacher.phone_number = self.cleaned_data['phone_number']

		if commit:
			user.save()

		return user '''

class EditProfileForm(UserChangeForm):
	
	class Meta:
		model = Profile
		fields = (
			'profile.phone_number',
			'email',
			'password'
		)

