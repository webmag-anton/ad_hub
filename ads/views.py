from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ad
from .models import AdImage


@login_required
def user_ads(request):
    # ads = Ad.objects.all()
    myAds = Ad.objects.filter(user=request.user).prefetch_related('images')
    context = {'myAds': myAds}

    return render(request, 'ads/index.html', context)