from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ad
from .models import AdImage


@login_required
def my_ads(request):
    myAds = Ad.objects.filter(user=request.user).prefetch_related('images')
    myAds_count = myAds.count()
    context = {
        'myAds': myAds, 
        'myAds_count': myAds_count
    }

    return render(request, 'ads/my_ads.html', context)


def get_ad(request, slug):
    # Ad.objects.get(slug=slug)
    ad = get_object_or_404(Ad, slug=slug)
    context = {'ad': ad}

    return render(request, 'ads/index.html', context)    