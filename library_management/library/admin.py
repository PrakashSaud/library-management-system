from django.contrib import admin
from .models import Student, Book, IssuedBook

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'user', 'isRegistered')


# we can use decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'edition', 'category', 'language')


admin.site.register(Student, StudentAdmin)
# admin.site.register(Book, BookAdmin)

admin.site.register(IssuedBook)
