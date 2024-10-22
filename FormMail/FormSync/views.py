from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm # Import the form
from .models import ContactMail  # and also Import the model

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #This is to save the message to the database
            contact_message = ContactMail.objects.create(
                    name = form.cleaned_data['name'],
                    email = form.cleaned_data['email'],
                    message = form.cleaned_data['message'],
            )

            #To send message to our preferred SMTP Provider(Gmail)
            send_mail(
                    f'New message submitted via the contact form by {contact_message.name}', # This will serve as the subject of the message upon recieving
                    contact_message.message, # The body of the message
                    contact_message.email, # From the email that sent the message
                    [settings.EMAIL_HOST_USER], # To the Email that will be recieving. (set at the settings.py file(Your email))
            )
            return redirect('message_sent') #Redirect to the success page
    else:
        form = ContactForm()

    context = {
        'title': 'We Would Love to Hear From You!',
        'form': form,
    }

    return render(request, 'pages/form.html', context)

def message_sent(request):
    context = {
        'title': 'Message Sent Successfully!'
    }
    return render(request, 'pages/success.html', context)