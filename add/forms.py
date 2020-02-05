from django import forms

class IDForm(forms.Form):
    Item_ID = forms.CharField()
class nameForm(forms.Form):
    Item_name = forms.CharField()
class priceForm(forms.Form):
    price = forms.CharField()
class search(forms.Form):
    Name_of_product = forms.CharField(required=False)
class Image(forms.Form):
    Image_url = forms.CharField()


