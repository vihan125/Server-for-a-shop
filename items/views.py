from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from add.forms import search


# Create your views here.



def read_file(request):
    if request.method =='POST':
        name = search(request.POST)
        
        if name.is_valid():
            name_text = name.cleaned_data['Name_of_product']
            

            f = open("items/storage.txt","r")
            content = f.read().split("\n")
            f.close()
            data=[]
            for each in content:
                s=''
                l=each.split(',')
                p=[]
                p.append(l[0])
                for i in range (1,len(l)-2):
                    if i<len(l)-3:
                        s = s + l[i]+','
                    else:
                        s= s+l[i]
                p.append(s)
                p.append(l[len(l)-2])
                p.append(l[len(l)-1])
                data.append(p)
            results=[]
            for i in range(0,len(data)):
                if name_text in data[i][1]:
                    results.append(data[i])
            template = loader.get_template('items/search.html')
            context ={
            'data':results
             }
            return HttpResponse(template.render(context,request))


                    
            

    else:
        f = open("items/storage.txt","r")
        content = f.read().split("\n")
        f.close()
        data=[]
        for each in content:
            s=''
            l=each.split(',')
            p=[]
            p.append(l[0])
            for i in range (1,len(l)-2):
                if i<len(l)-3:
                    s = s + l[i]+','
                else:
                    s= s+l[i]
            p.append(s)
            p.append(l[len(l)-2])
            p.append(l[len(l)-1])
            data.append(p)
        template = loader.get_template('items/index.html')
        name = search(request.POST)
        context ={
            'data':data,'name':name
        }

    return HttpResponse(template.render(context,request))

