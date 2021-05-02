from django.shortcuts import render, redirect
from .forms import ContactForm, CommentForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    print('*** index ***'* 20)
    return render(request, 'home/home.html', context = context)

def post_review(request, id):
    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post = post, user = request.user, content = content)
            comment.save()
        else:
            cf = CommentForm()

        context = {
        'comment_form':cf,
        }
        return render(request, 'home:reviews', context  )

def contactForm(request):
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
    return render(request, "home/contact.html", {'form,':forms})

# Create your views here.
