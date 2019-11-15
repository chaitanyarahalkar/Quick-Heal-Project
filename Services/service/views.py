from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib import messages


def home(request):
    return HttpResponse('Hello, World!')

def register(request):
    if request.method == 'POST':
        
        header_dict = dict(request.headers.items())
        if not "Authorization" in header_dict.keys():
            return redirect("http://127.0.0.1:8000/")

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return HttpResponse("Logged In")
    else:
        form = UserRegisterForm()
    return render(request, 'service/index.html', {'form': form})



