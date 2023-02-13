from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# def add_book(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         author = request.POST['author']
#         writer = request.POST['witer']
#         publication_date = request.POST['publication_date']
#         Book.objects.create(title=title, author=author, publication_date=publication_date, price=price)
#         return redirect('book_list')
#     return render(request, 'books/add_book.html')

# def delete_book(request, book_id):
#     Book.objects.get(id=book_id).delete()
#     return redirect('book_list')

# def update_book(request, book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == 'POST':
#         book.title = request.POST['title']
#         book.author = request.POST['author']
#         book.publication_date = request.POST['publication_date']
#         book.price = request.POST['price']
#         book.save()
#         return redirect('book_list')
#     return render(request, 'books/update_book.html', {'book': book})
