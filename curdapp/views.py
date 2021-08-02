
from django.shortcuts import redirect, render
from curdapp import form
from curdapp.form import Userform
from django.http import HttpResponse
from curdapp.models import user


# Create your views here.
def insert(request):
    if request.method=='POST':
        forms=Userform(request.POST)
        if forms.is_valid:
            try:
                forms.save()
                return HttpResponse("this is saved")
            except:
                pass
    formss=Userform()
    return render(request,'index.html',{'forms':formss})

def show(request):
 users=user.objects.all()
 return render(request,'show.html',{'user':users})


def delete(request,id):
    users=user.objects.get(id=id)
    users.delete()
    return redirect('/show')

def edit(request,id):
    users=user.objects.get(id=id)
    return render(request,'edit.html',{'users':users})
def update(request,id):
    users=user.objects.get(id=id)
    forms=Userform(request.POST,instance=users)
    if forms.is_valid():
        forms.save()
        return redirect('/show')
    return render(request,'edit.html',{{'users':users}})       