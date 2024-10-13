from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from Plants.models import Houseplants
from .models import Cart,CartItrm
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

#def homeCarts(request):
#    return render(request=request,template_name="carts.html")


#def cart_detail(request):
#    plants=Houseplants.objects.all()
#    return render(request=request,template_name="carts.html",context={"plants":plants})

def cart_detail(request):
    query=request.GET.get('q')
    if query:
        plants=Houseplants.objects.filter(name=query)
    else:
        plants = Houseplants.objects.all()

    return render(request=request, template_name="carts.html", context={"plants": plants})

@login_required(login_url="/Users/")
def add_to_cart(request,plant_id):
    plant = get_object_or_404(Houseplants, id=plant_id)
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_item,created=CartItrm.objects.get_or_create(cart=cart,plant=plant)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect("manage_cart")

@login_required(login_url="/Users/")
def manage_cart(request):
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_items =CartItrm.objects.filter(cart=cart)
    total_price = sum(item.plant.price * item.quantity for item in cart_items)
    return render(request=request,template_name="managecarts.html",context={"cart_items":cart_items,"total_price":total_price})

def remove_from_cart(request,item_id):
    cart_item= get_object_or_404(CartItrm,id=item_id,cart__user=request.user)
    cart_item.delete()
    return redirect("manage_cart")

def checkoutt(request):
    return render(request=request,template_name="thanks.html")

def remove_from_all_cart(request):
    cart_it = CartItrm.objects.all()
    cart_it.delete()
    return redirect("manage_cart")

