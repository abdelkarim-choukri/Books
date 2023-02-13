"""booklist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from books.views  import book_list
import books.views
import book_auth.views
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView
from book_auth.forms import BookRegistrationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books.views.book_list, name='book_list'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", book_auth.views.profile, name="profile"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BookRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("add_book/", book_auth.views.add_book, name="add_book"),
    path('delete_book/<int:pk>/', book_auth.views.delete_book.as_view(),name="delete_book"),
    path("update_book/<int:pk>/", book_auth.views.update_book.as_view(),name='update_book'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)