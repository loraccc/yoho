from django.shortcuts import render,redirect
from .forms import personform
from .models import person,Image
# Create your views here.
def index(request):
    per=person.objects.all()
    # images=Image.objects.all()
    if request.method=='POST' and request.FILES:
        image=request.FILES['img']
        user=Image(img=image)
        user.save()
    images=Image.objects.all()
    context={
            'std_list':per,
            'images':images,
        }
    return render(request,'index.html',context)

def create(request):
    form=personform()
    context={'form':form}
    return render(request,'create.html',context)
def upload(request,id):
    images=Image.objects.filter(id=id)
    context={'images':images
    }
    if request.method=='POST' and request.FILES:
        image=request.FILES['img']
        user=Image(img=image)
        user.save()
        
    return render(request,'upload.html',context)