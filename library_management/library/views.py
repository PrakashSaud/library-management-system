from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import NewUserForm, StudentForm, BookForm, IssueBookForm
from .models import Book, Student, IssuedBook
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone


# Create your views here.
class AllBooksListView(generic.ListView):
    model = Book
    template_name = 'library/all_book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'


class BookAddView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'category', 'language', 'edition']
    template_name = 'library/book_add_form.html'
    # success_url = reverse_lazy('book_add')

    def get_success_url(self):
        return reverse('all_book_list')


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'category', 'language', 'edition']
    template_name = 'library/book_update_form.html'

    def get_success_url(self):
        return reverse('all_book_list')

    # def get_success_url(self, **kwargs):
    #     return reverse('book_detail', kwargs={'id': self.object.pk})


# Using function Based view
# def book_update(request, book_id):
#     if request.method == "POST":
#         book_obj = Book.objects.get(pk=book_id)
#         form = BookForm(request.POST, instance=book_obj)
#         if form.is_valid():
#             form.save()
#         else:
#             form = BookForm()
#         return render(request, 'library/book_update_form.html', {'form': form})


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'library/book_delete_form.html'

    success_url = reverse_lazy('all_book_list')


def issued_book_list(request):
    books = IssuedBook.objects.all()
    return render(request, 'library/issued_book_list.html', {'issued_books': books})


# this method issue the book for a student
def book_issue(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['name']
            student = form.cleaned_data['issued_to']
            issued_time = form.cleaned_data['issued_date']
            issued_book_obj = IssuedBook(name=book, issued_to=student, issued_date=issued_time)
            issued_book_obj.save()
            form = IssueBookForm()
    else:
        form = IssueBookForm()
    return render(request, 'library/issue_book_form.html', {'issue_form':form})


# STUDENT RELATED VIEWS
def add_new_student(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        user = form.cleaned_data['user']
        registration = form.cleaned_data['isRegistered']
        Student.objects.create(name=name,
                           email=email,
                           phone=phone,
                           user=user,
                           isRegistered=registration)
        return HttpResponseRedirect(reverse('all_student_list'))
    else:
        form = StudentForm()
    return render(request, 'library/student_add_form.html', {'student_form': form})


class AllStudentListView(generic.ListView):
    model = Student
    template_name = "library/all_student_list.html"


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'library/student_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['due_amount'] = Student.due_amount(self)
    #     return context


# if student want to register to issue books
def register_student(request, **kwargs):
    student = get_object_or_404(Student, pk=kwargs['pk'])
    student.register()
    return redirect('student_detail', pk=kwargs['pk'])


# Authentication

def register_request(request):
    error_message = ""
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            error_message = form.errors
    form = NewUserForm()
    return render(request, 'library/register.html', context={"register_form": form, "error_message": error_message})


def login_request(request):
    message = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = "You're now logged In"
                return HttpResponseRedirect(reverse('all_student_list'))
            else:
                message = "Invalid Username or Password"
        else:
            message = form.errors
    form = AuthenticationForm()
    return render(request, "library/login.html", context={"login_form": form, "message": message})


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))