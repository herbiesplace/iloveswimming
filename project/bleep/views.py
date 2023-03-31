from django.shortcuts import render,redirect
from .models import InteresanteLink
from django.contrib.auth.decorators import login_required 
from main.decorators import user_is_superuser
from django.views.decorators.csrf import csrf_exempt
from .forms import LinkForm

def links(request):
    links = InteresanteLink.objects.all()
    return render(request, 'bleep/links.html' , {"links":links})

@user_is_superuser
def new_link(request): 
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        form = LinkForm()

    return render(request,'bleep/new_link.html',{"form": form})