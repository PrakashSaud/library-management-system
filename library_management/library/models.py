from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)
    isRegistered = models.BooleanField(default=False)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.title + "-- by --" + self.author


class IssuedBook(models.Model):
    name = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    issued_to = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="students")
    issued_date = models.DateTimeField('issued_date', auto_now_add=True)
    expire_date = models.DateTimeField('expire_date', default=datetime.today() + timedelta(days=15))

    def get_fine_amount(self):
        """Once the book issued after 15 days the fine amount will be added
        $5 everyday"""
        days_of_fine = self.expire_date - self.issued_date
        if days_of_fine > 0:
            fine_amount = days_of_fine * 5
            return fine_amount
        return 0
