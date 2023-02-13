from django import forms
from books.models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','writer','pdf']
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))
