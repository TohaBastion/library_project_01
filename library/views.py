from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *


def home(request):
    return render(request, 'library/home.html')


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'library/add_author.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'library/author_detail.html', {'author': author})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


def update_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/update_author.html', {'form': form})


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/update_book.html', {'form': form})


def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'library/delete_author.html', {'author': author})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/delete_book.html', {'book': book})
