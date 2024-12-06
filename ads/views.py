from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
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
    user = get_object_or_404(User, id=id)
    userAds = Ad.objects.filter(user=user).prefetch_related('images')
    userAds_count = userAds.count()
    context = {
        'user': user,
        'userAds': userAds, 
        'userAds_count': userAds_count
    }

    return render(request, 'ads/user_ads.html', context)    


def get_ad(request, slug):
    # Ad.objects.get(slug=slug)
    ad = get_object_or_404(Ad, slug=slug)
    context = {'ad': ad}

    return render(request, 'ads/index.html', context)    