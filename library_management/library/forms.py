from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Student


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'edition', 'category', 'language')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'user', 'isRegistered']
        labels = {'name': 'Enter Name',
                  'email': 'Email',
                  'phone': 'Phone',
                  'user': 'User',
                  'isRegistered': 'Registraion'
                  }
        help_text = {'name': "Enter Your Full Name"}
        error_messages = {'name': {'required': 'Name is mandatory'}
                          }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name here'})}
