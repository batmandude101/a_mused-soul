from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username},You can login now')
            return redirect('login')
    else:    
        form = UserRegistration()
    return render(request, 'users/registeration.html' , {'form':form} )
