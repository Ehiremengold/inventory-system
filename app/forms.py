from django import forms
from .models import Laptop, Mobile, Desktop

class LaptopForm(forms.ModelForm):

    class Meta:
        model = Laptop
        fields = "__all__"


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = "__all__"


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"