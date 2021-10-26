from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def logout(request):
    """log out page"""
    return render(request, 'registration/logged_out.html')

def register(request):
    """Registration of a new user"""
    if request.method != "POST":
        """Empty form for reg"""
        form = UserCreationForm()
    else:
        """Filled form """
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Redirection to homepage
            login(request, new_user)
            return redirect('index')

    # broken form
    context = {'form': form}
    return render(request,'registration/register.html', context)
