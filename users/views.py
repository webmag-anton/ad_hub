from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserProfileForm


"""
Authenticated user with authorisation can open own profile page.
"""
@login_required
def profile_page(request):
    user = request.user
    context = {'user': user}

    return render(request, 'users/index.html', context)    


"""
Authenticated user with authorisation can open a page to edit own profile.
"""
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'users/edit_profile.html', {'form': form})    