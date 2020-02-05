from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from add.forms import IDForm

## have to make changes


# Create your views here.

def delete(request):
    if request.method =='POST':
        ID = IDForm(request.POST)
    

        if ID.is_valid():
            text_ID = ID.cleaned_data['Item_ID']
            

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
            
            for i in range(0,len(data)):
                if data[i][0]==text_ID:
                    data.pop(i)
                    break
            else:
                ID = IDForm()
                error = "sorry the entered Item ID cannot be found"
                return render(request,"add/add.html",{'ID':ID,'error':error}) 
            
            f = open("items/storage.txt","w")

            for each in data:
                if data.index(each)==len(data)-1:
                    write = each[0]+","+each[1]+","+each[2]+","+each[3]
                    f.write(write)
                else:
                    write = each[0]+","+each[1]+","+each[2]+","+each[3]+"\n"
                    f.write(write)
            
            f.close()
            return redirect("home")

    else:
        ID = IDForm()
    return render(request,"delete/delete.html",{'ID':ID})
