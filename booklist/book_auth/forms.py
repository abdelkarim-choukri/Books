from django_registration.forms import RegistrationForm
from book_auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(BookRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))

        