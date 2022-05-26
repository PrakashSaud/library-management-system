from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, default='admin@admin.com')
    phone = models.IntegerField(default=1234567890)
    user = models.OneToOneField(User, on_delete=models.RESTRICT, blank=True, null=True)
    isRegistered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    category_choices = [
        ('programming', 'Programming'),
        ('science', 'Science'),
        ('history', 'History'),
        ('biography', 'Biography'),
        ('novel', 'Novel'),
        ('mathematics', 'Mathematics')
    ]
    language_choices = [
        ('english', 'English'),
        ('chinese', 'Chinese'),
        ('hindi', 'Hindi'),
        ('nepali', 'Nepali'),
        ('other', 'Other')
    ]
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    edition = models.IntegerField(default=1)
    category = models.CharField(max_length=20, choices=category_choices, default='programming')
    language = models.CharField(max_length=20, choices=language_choices, default="english")

    # def __str__(self):
    #     return self.title + "-- by --" + self.author

    class Meta:
        ordering = ['title']


class IssuedBook(models.Model):
    name = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    issued_to = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="students")
    issued_date = models.DateTimeField('issued_date', auto_now_add=True)
    # expire_date = models.DateTimeField('expire_date', default=issued_date + timedelta(days=15))

    def __str__(self):
        return str(self.name.title) + " -- issued to -- " + str(self.issued_to.name)

    def issue(self):
        self.issued_date = timezone.now()
        self.issued_to = Student()
        self.save()

    def get_fine_amount(self):
        """Once the book issued after 15 days the fine amount will be added
        $5 everyday"""
        days_of_fine = timezone.now() - self.issued_date
        if days_of_fine > 0:
            fine_amount = days_of_fine * 5
            return fine_amount
        return 0
