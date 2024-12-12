from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import timedelta
from .models import Ad, AdImage
from users.models import User
from .forms import AdForm, AdImageForm


@login_required
def my_ads(request):
    myAds = Ad.objects.filter(user=request.user).order_by('-created_at').prefetch_related('images')
    myAds_count = myAds.count()
    paginator = Paginator(myAds, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'myAds': myAds, 
        'myAds_count': myAds_count,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }

    return render(request, 'ads/my_ads.html', context)


def user_ads(request, id):
    info_user = get_object_or_404(User, id=id)
    userAds = Ad.objects.filter(user=info_user).order_by('-created_at').prefetch_related('images')
    userAds_count = userAds.count()
    paginator = Paginator(userAds, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info_user': info_user,
        'userAds': userAds, 
        'userAds_count': userAds_count,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }

    return render(request, 'ads/user_ads.html', context)    


def get_ad(request, slug):
    ad = get_object_or_404(Ad, slug=slug)
    existing_images = ad.images.all()
    remaining_images = 5 - existing_images.count()
    remaining_range = range(remaining_images)
    ad_form = AdForm(instance=ad)
    image_form = AdImageForm()
    now = timezone.now()
    time_difference_in_minutes = (ad.updated_at - ad.created_at).total_seconds() / 60 if ad.updated_at and ad.created_at else 0

    context = {
        'ad': ad,
        'time_difference_in_minutes': time_difference_in_minutes,
        # for edit form in popup:
        'ad_form': ad_form,
        'image_form': image_form,
        'existing_images': existing_images,
        'remaining_range': remaining_range,
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
                'You have created a new ad!'
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


@login_required
def edit_ad(request, slug):
    ad = get_object_or_404(Ad, slug=slug)

    if ad.user != request.user:
        messages.error(request, "You are not authorized to edit this ad.")
        return redirect('')

    if request.method == 'POST':
        ad_form = AdForm(request.POST, instance=ad)
        image_form = AdImageForm(request.POST, request.FILES)
        
        if ad_form.is_valid() and image_form.is_valid():
            ad_form.save()

            for image_instance in ad.images.all():
                delete_image_key = f'delete_image_{image_instance.id}'
                if delete_image_key in request.POST:
                    image_instance.delete()

            for img in request.FILES.getlist('image'):
                AdImage.objects.create(ad=ad, image=img)

            messages.success(request, "Ad updated successfully!")
            return redirect('ad', slug=ad.slug)
        else:
            messages.error(request, "There was an error updating the ad.")
    else:
        ad_form = AdForm(instance=ad)
        image_form = AdImageForm()

    context = {
        'ad_form': ad_form,
        'image_form': image_form,
        'ad': ad,
    }

    return render(request, 'ads/index.html', context)    


def search_ads(request):
    query = request.GET.get('q')
    if query:
        ads = Ad.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        ).order_by('-created_at')
    else:
        ads = Ad.objects.all().order_by('-created_at')

    ads_count = ads.count()    
    
    context = {
        'ads': ads,
        'query': query,
        'ads_count': ads_count
    }

    return render(request, 'ads/search_results.html', context)
