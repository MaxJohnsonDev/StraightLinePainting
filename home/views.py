from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_email, BadHeaderError
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email'],
            'phone_number': form.cleaned_data['phone_number'],
            'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect ("home:contactForm")
    form = ContactForm()
    return render(request, "home/contact.html", {'for,':forms})

# Create your views here.
