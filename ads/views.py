from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from .models import Ad
from .models import AdImage
from users.models import User


@login_required
def my_ads(request):
    myAds = Ad.objects.filter(user=request.user).prefetch_related('images')
    myAds_count = myAds.count()
    context = {
        'myAds': myAds, 
        'myAds_count': myAds_count
    }

    return render(request, 'ads/my_ads.html', context)


def user_ads(request, id):
    info_user = get_object_or_404(User, id=id)
    userAds = Ad.objects.filter(user=info_user).prefetch_related('images')
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