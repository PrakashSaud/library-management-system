from django.contrib import admin
from .models import Student, Book, IssuedBook

# Register your models here.
admin.site.register([Student, Book, IssuedBook])