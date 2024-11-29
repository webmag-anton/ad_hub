from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserProfileForm


def home_page(request):
    return render(request, 'ads/index.html')


def profile_page(request):
    # users = User.objects.all()
    user = request.user
    context = {'user': user}

    return render(request, 'users/index.html', context)    
    

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