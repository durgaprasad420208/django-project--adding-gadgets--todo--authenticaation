from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, ("Submitted successfully, we will get back to you soon..."))
            return redirect('home')

    else:
        form = ContactForm()

    title = "Contact us"
    template = "contact/contact_us.html"
    context = {
        "title": title,
        "form": form
    }
    return render(request, template, context)
