from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import IDForm,nameForm,priceForm,Image


# Create your views here.

def add(request):
    if request.method =='POST':
        ID = IDForm(request.POST)
        name = nameForm(request.POST)
        price = priceForm(request.POST)
        image = Image(request.POST)

        if (ID.is_valid() and name.is_valid() and price.is_valid() and image.is_valid()):
            text_ID = ID.cleaned_data['Item_ID']
            text_name = name.cleaned_data['Item_name']
            price_text = price.cleaned_data['price']
            url = image.cleaned_data['Image_url']

            f = open("items/storage.txt","a")
            data = "\n"+text_ID +','+text_name+','+price_text+','+url
            f.write(data)
            f.close()
            return redirect("home")

    else:
        ID = IDForm()
        name = nameForm()
        price = priceForm()
        image = Image()
    return render(request,"add/add.html",{'ID':ID,'name':name,'price':price,'image':image})


 
    

    