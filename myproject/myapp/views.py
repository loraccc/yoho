from django.shortcuts import render,redirect
from .forms import personform
from .models import person,Image
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate 
from django.contrib.auth.decorators import login_required 

from django.template.loader import render_to_string
from django.core.mail import send_mail
from .serializers import UserSerializer
from rest_framework import generics
# Create your views here.
#api
class PersonList(generics.ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = UserSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = person.objects.all()
    serializer_class = UserSerializer
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email=request.POST['email']
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password1)
                message = render_to_string('email.html')
                send_mail(
                subject="User Registration", # subject
                message=message,
                from_email="carolacharya1@gmail.com", # sender
                recipient_list=[email], # receiver,
                fail_silently=False,
                html_message=message, # message
            )
            login(request, user)
            return redirect('index')
    return render(request,'register.html')
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
        
    return render(request,'login.html')

# @login_required
def index(request):
    per=person.objects.all().order_by('-name')
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
def upload(request):
    images=Image.objects.all()
    context={'images':images
    }
    if request.method=='POST' and request.FILES:
        image=request.FILES['img']
        user=Image(img=image)
        user.save()
        
    return render(request,'upload.html',context)
def email(request):
    if request.method=='POST':
        username=request.POST['username']
        age=request.POST['age']
        email=request.POST['email']
        address=request.POST['address']
        a=person(username=username,age=age,email=email,address=address)
        a.save()
        return redirect('index')
    return render(request,'login.html')
from .models import Cart

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = int(request.POST.get('quantity', 1))

        cart_item = Cart(item_name=item_name, quantity=quantity)
        cart_item.save()

        return redirect('cart')

    return render(request, 'add_to_cart.html')