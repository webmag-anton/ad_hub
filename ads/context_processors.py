from .forms import AdForm, AdImageForm

def ad_form_processor(request):
    ad_form = AdForm()
    image_form = AdImageForm()
    return {
        'ad_form': ad_form,
        'image_form': image_form
    }