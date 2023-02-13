from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect 
from books.models import Book
from books.forms import BookForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def profile(request):
    # Retrieve only the books belonging to the specified author
    books = Book.objects.filter(author=request.user)
    return render(request, 'book_auth/profile.html',{'books': books}) # {'books': books}

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.publication_date = timezone.now()# or  in model auto_now_add=True
            book.save()
            return redirect('profile') # use the name that you make in the url to call the view ==> template 
    else:
        form = BookForm()

    context = {
        'form': form,
    }
    return render(request, 'book_auth/add_book.html', context)


# class delete_book(DeleteView,LoginRequiredMixin):
#     model = Book
#     success_url = reverse_lazy('profile')
#     template_name = 'book_auth/delete_book.html'

    


class delete_book(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('profile')
    template_name = 'book_auth/delete_book.html'

    def get_object(self, queryset=None):
        book = super().get_object(queryset)
        if not book:
            raise Http404("No book found matching the query")
        return book




# @login_required
# def update_book(request,pk):
#     book=Book.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES, instance=book)
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.author = request.user
#             book.publication_date = timezone.now()# or  in model auto_now_add=True
#             book.save()
#             return redirect('profile') # use the name that you make in the url to call the view ==> template 
#     else:
#         form = BookForm(instance=book)

#     context = {
#         'form': form,
#     }
#     return render(request, 'book_auth/update_book.html', context)


class update_book(LoginRequiredMixin,UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('profile')
    template_name = 'book_auth/update_book.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.publication_date = timezone.now() # or  in model auto_now_add=True
        return super().form_valid(form)
    


