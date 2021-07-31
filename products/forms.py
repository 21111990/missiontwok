from django import forms
from .models import Product,Productinshop


class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name","price","stock", "image1","Product_id","image")
class ImageForm_shop(forms.ModelForm):
    class Meta:
        model = Productinshop
        fields = ("Product_name","image1")

