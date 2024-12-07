from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from datetime import timedelta
from .models import Ad, AdImage
from users.models import User
from .forms import AdForm, AdImageForm


@login_required
def my_ads(request):
    myAds = Ad.objects.filter(user=request.user).order_by('-created_at').prefetch_related('images')
    myAds_count = myAds.count()
    context = {
        'myAds': myAds, 
        'myAds_count': myAds_count
    }

    return render(request, 'ads/my_ads.html', context)


def user_ads(request, id):
    info_user = get_object_or_404(User, id=id)
    userAds = Ad.objects.filter(user=info_user).order_by('-created_at').prefetch_related('images')
    userAds_count = userAds.count()
    context = {
        'info_user': info_user,
        'userAds': userAds, 
        'userAds_count': userAds_count
    }

    return render(request, 'ads/user_ads.html', context)    


def get_ad(request, slug):
    ad = get_object_or_404(Ad, slug=slug)
    now = timezone.now()
    time_difference_in_minutes = (ad.updated_at - ad.created_at).total_seconds() / 60 if ad.updated_at and ad.created_at else 0
    context = {
        'ad': ad,
        'time_difference_in_minutes': time_difference_in_minutes,
    }

    return render(request, 'ads/index.html', context)    


@login_required
def create_ad(request):
    if request.method == 'POST':
        ad_form = AdForm(request.POST)
        image_form = AdImageForm(request.POST, request.FILES)
        
        if ad_form.is_valid() and image_form.is_valid():
            ad = ad_form.save(commit=False)
            ad.user = request.user
            if not ad.description or ad.description.strip() == '':
                ad.description = 'No description'
            ad.save()

            ad_form.save_m2m()

            for img in request.FILES.getlist('image'):
                AdImage.objects.create(ad=ad, image=img)

            messages.add_message(
                request, messages.SUCCESS,
                'Add created !!!'
            )
            return redirect('my_ads')
        else:
            messages.error(request, "There was an error in the form submission.")    
    else:
        ad_form = AdForm()
        image_form = AdImageForm()

    context = {
        'ad_form': ad_form,
        'image_form': image_form
    }

    return render(request, 'ads/index.html', context)


@login_required
def delete_ad(request, slug):
    ad = get_object_or_404(Ad, slug=slug)

    if ad.user != request.user:
        messages.error(request, "You are not authorized to delete this ad.")
        return redirect('')

    if request.method == 'POST':
        ad.delete()
        messages.success(request, "Your ad has been successfully deleted.")
        return redirect('my_ads')

    return render(request, 'ads/index.html', {'ad': ad})    