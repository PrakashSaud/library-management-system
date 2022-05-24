from django.shortcuts import render
from django.views import generic
from .models import Book
from django.urls import reverse, reverse_lazy


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
    template_name = 'library/book_update_form.html'
    fields = ['title', 'author', 'category', 'language', 'edition']

    def get_success_url(self):
        return reverse('book_detail')


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'library/book_delete_form.html'

    success_url = reverse_lazy('all_book_list')