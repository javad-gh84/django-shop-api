from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def index(request):
    return render(request, 'core/index.html')


def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            surname=request.POST.get('surname'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'پیام شما با موفقیت ارسال شد! ✅')
        return redirect('core:contact')

    return render(request, 'core/contact.html')