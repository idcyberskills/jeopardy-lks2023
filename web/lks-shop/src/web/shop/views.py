from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as djlogin, logout as djlogout
from shop.models import User, Profile, Item
from django.contrib import messages
from django.db.utils import IntegrityError
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

import os
import requests
import uuid

def index(request):
    return render(request, "index.html")

def register(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            if not username or not password:
                raise Exception("Username and password cannot be empty")
            if len(password) < 8 or password.find(username) != -1:
                raise Exception("Password length cannot less than 8 characters and cannot contain username")
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()
            new_profile = Profile(user=new_user)
            new_profile.save()
            messages.success(request, "Registered successfully")
    except IntegrityError as e:
        messages.error(request, "Username already existed")
    except Exception as e:
        messages.error(request, str(e))

    return render(request, "register.html")

def login(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            auth_user = authenticate(username=username, password=password)
            if not auth_user:
                raise Exception("Username or password is wrong")
            djlogin(request, auth_user)
            return redirect("/")
    except IntegrityError as e:
        messages.error(request, "Username already used")
    except Exception as e:
        messages.error(request, str(e))

    return render(request, "login.html")

@login_required
def logout(request):
    djlogout(request)
    return redirect(reverse('login'))

@login_required
def tambah_duit(request):
    user = User.objects.get(username='admin')
    profile = Profile.objects.get(user=user)
    if profile.money < 1000000000:
        profile.money = 1000000000
        profile.save()
    return redirect('/')

@login_required
def show_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "profile.html", {'profile': profile})

@login_required
def update_profile(request):
    try:
        if request.method == "POST":
            profile = Profile.objects.get(user=request.user)
            image = request.FILES['image']
            handle_uploaded_file(image, profile)
            return redirect(reverse('show_profile'))
    except Exception as e:
        messages.error(request, str(e))
    return render(request, "update_profile.html")

def handle_uploaded_file(f, profile):
    BASE_DIR = os.getenv("PHOTO_BASE_DIR", "static/image/photo")
    ALLOWED_FILES = ['jpeg', 'jpg', 'png', 'bimp', 'svg', 'bmp', 'gif']
    if f.size > (10 ** 6):
        raise Exception("file size too large")
    if f.name.split(".")[-1] not in ALLOWED_FILES:
        raise Exception("file extension is not allowed")
    fext = f.name.split(".")[-1]
    kode = profile.image.split(".")[0]
    if kode == "default":
        kode = uuid.uuid4()
    with open(f"{BASE_DIR}/{kode}.{fext}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    profile.image = f"{kode}.{fext}"
    profile.save()

@login_required
@require_POST
def buy_product(request, id):
    try:
        buyer = Profile.objects.get(user=request.user)
        item = Item.objects.get(item_id=id)
        seller = Profile.objects.get(user=item.owner)
        quantity = int(request.POST.get("quantity", 0))
        
        if buyer.user == seller.user:
            raise Exception("You cannot buy your products")

        if quantity <= 0 or quantity > 1000000:
            raise Exception("Quantity must positive integer and not more than 1000000")
        
        cost = item.price * quantity
        if buyer.money < cost:
            raise Exception("Your money is insufficient")
        
        buyer.money -= cost
        buyer.bought.add(item)
        buyer.save()
        
        seller.money += cost
        seller.save()

        messages.success(request, "Order received successfully")
    except ValueError:
        messages.error(request, "Quantity must an integer")
    except Exception as e:
        messages.error(request, str(e))
    return render(request, "buy_item.html", {"item_id": id})

@login_required
def create_product(request):
    try:
        if request.method == "POST":
            price = int(request.POST.get("price","0"))
            title = request.POST.get("title", "")
            description = request.POST.get("description", "")
            if price <= 0 or price > 1000000:
                raise Exception("Product price must positive integer and not more than 1000000")
            item = Item(title=title, description=description, price=price, owner=request.user)
            item.save()
            messages.success(request, "Successfully add new product")
    except ValueError:
        messages.error(request, "Quantity must an integer")
    except Exception as e:
        messages.error(request, str(e))
    return render(request, "add_item.html")

@login_required
def show_product(request, id):
    item = Item.objects.get(item_id=id)
    item.description = item.description.replace("\n", "<br>")
    return render(request, "show_item.html", {'item': item})

@login_required
def list_my_product(request):
    items = Item.objects.filter(owner=request.user)
    return render(request, "list_items.html", {"page_title": "My Products", "items": items})

@login_required
def list_featured_product(request):
    items = Item.objects.filter(owner__username="admin")
    return render(request, "list_items.html", {"page_title": "Featured Products", "items": items})

@login_required
def get_flag(request):
    profile = Profile.objects.get(user=request.user)
    numbuy_flag = profile.bought.filter(pk=1).count()
    if numbuy_flag == 0:
        messages.error(request, "You are not eligible to access the flag. Buy the product first!")
    else:
        with open("flag.txt") as flag:
            messages.success(request, "Your flag: " + flag.read())
    return render(request, "flag.html")

@login_required
def report_product(request, id):
    try:
        item_url = reverse('show_product', kwargs={"id": id})
        ADMIN_REPORT_URL = os.getenv("ADMIN_REPORT_URL", "http://xssbot:5000/visit")
        HOST_URL = os.getenv("HOST_URL", "http://web:80")
        requests.post(ADMIN_REPORT_URL, json={'url': f'{HOST_URL}{item_url}'})
        messages.success(request, "Thank you for your report!")
    except Exception as e:
        print(e)
        messages.error(request, "Failed to send your report")
    return redirect(item_url)