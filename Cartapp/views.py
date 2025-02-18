from django.shortcuts import render,redirect
from .models import *
from Category.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def add_to_cart(request,item_id):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cartitem,created=Cart_Items.objects.get_or_create(user=request.user,item=Product.objects.get(id=item_id))

    if not created:
        cartitem.quantity+=1
        cartitem.save()

    return redirect('/cart/viewcart/')


@login_required(login_url='login')

def viewcart(request):
    cartitems = Cart_Items.objects.filter(user=request.user)
    total_price = sum(item.item.price * item.quantity for item in cartitems)
    return render(request, 'viewcart.html', {'cartitems': cartitems, 'total_price': total_price})

@login_required(login_url='login')
def remove_from_cart(request, item_id):
    # Use filter() to check if the cart item exists
    cartitem = Cart_Items.objects.filter(user=request.user, item_id=item_id).first()

    if cartitem:
        # Decrease quantity or delete the item
        if cartitem.quantity > 1:
            cartitem.quantity-=1
            cartitem.save()
        else:
            cartitem.delete()

    # If cart item doesn't exist, silently redirect to the cart page
    return redirect('/cart/viewcart/')




def search_category(request):
    query=request.GET['r']
    data=Product.objects.filter(name__icontains=query)
    return render(request,'search.html',{'data':data})