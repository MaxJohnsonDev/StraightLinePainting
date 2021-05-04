from django.shortcuts import render, redirect
from .forms import ContactForm, CommentForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def home_view(request):
    print('*** index ***'* 20)
    return render(request, 'home/home.html')

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
    return render(request, 'home:contactForm', {'form,':forms})


def displayReviews(request):
    print('*** displayReviews ***' * 10)
# Create your views here.

def contactFormSubmission(request):
    form_class = ContactForms

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_firstName = request.POST.get('first_name', '')
            contact_lastName = request.POST.get('last_name', '')
            contact_email = request.POST.get('email', '')
            contact_number = request.POST.get('phone_number', '')
            form_content = request.POST.get('message', '')

            template = get_template('contact_template.txt')
            context = {
                'contact_firstName': contact_firstName,
                'contact_lastName': contact_lastName,
                'contact_email': contact_email,
                'contact_number': phone_number,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your Website" + '',
                ['yourname@email.com'],
                headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')
    return render(request, 'contactForm.html', {'form':form_class,})
