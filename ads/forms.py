from django import forms
from .models import Ad, AdImage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget
from categories.models import Category


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'location', 'condition', 'categories']
        widgets = {
            'description': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.filter(parent__isnull=False)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Ad'))   
     

class AdImageForm(forms.ModelForm):
    delete_image = forms.BooleanField(required=False, label='Delete this image', initial=False)

    class Meta:
        model = AdImage
        fields = ['image', 'delete_image']