from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .forms import ContactForms

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            
            message_name = form.cleaned_data['message_name']
            message_email = form.cleaned_data['message_email']
            message = form.cleaned_data['message']
            send_mail(
               'Demande de contact de '+ str(message_name) + '- '+str(message_email) ,# subject
               message, # message
               message_email, # from email
               ['rhaiti.jamal@gmail.com'], # to email
               )
            
            return render(request,'home/index.html',{})
        
    else:
        form = ContactForms()
        
        context = {"form":form}
        return render(request,'home/index.html',context)

