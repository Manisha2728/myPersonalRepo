"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Contact
from .models import Student

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    # Retrieve all contacts in the database table
    contact_list = Contact.objects.order_by('name') 

    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'contact_list': contact_list, # Embed data into the HttpResponse object
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def student(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    # Retrieve all contacts in the database table
    student_list = Contact.objects.order_by('name') 

    return render(
        request,
        'app/contact.html',
        {
            'title':'student',
            'message':'List of students.',
            'year':datetime.now().year,
            'student_list': student_list, # Embed data into the HttpResponse object
        }
    )
