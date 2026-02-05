from django import forms
from listing.models  import Property

from listing.models import Enquiry

class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['phone_number','email','message']