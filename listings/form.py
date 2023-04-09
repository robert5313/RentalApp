from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'price',
            'description',
            'num_bedrooms',
            'num_bathrooms',
            'address',
            'location',
            'image'
        ]