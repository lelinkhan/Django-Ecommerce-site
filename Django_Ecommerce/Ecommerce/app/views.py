from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerRegistrationForm, CustomerProfileForm
from .models import *
from django.contrib.auth.decorators import login_required


def home(request):
    total_cart = 0
    phone = Product.objects.filter(category='M')
    laptops = Product.objects.filter(category='L')
    topwears = Product.objects.filter(category='TW')
    bottomwears = Product.objects.filter(category='BW')
    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))

    context = {
        'phone': phone,
        'laptop': laptops,
        'topwears': topwears,
        'bottomwears': bottomwears,
        'total_cart': total_cart
    }
    return render(request, 'app/home.html', context)


def product_detail(request, pk):
    total_cart = 0
    product = Product.objects.get(id=pk)
    item_exist = False
    if request.user.is_authenticated:
        item_exist = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {
        'product': product,
        'item_exist': item_exist,
        'total_cart': total_cart
    }
    return render(request, 'app/productdetail.html', context)


@login_required()
def add_to_cart(request, pk):
    user = request.user
    product = Product.objects.get(id=pk)
    cart = Cart(user=user, product=product)
    cart.save()
    return redirect('/cart')


@login_required()
def show_cart(request):
    total_cart = 0
    if request.user.is_authenticated:
        user = request.user
        carts = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 100.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp = p.quantity * p.product.discount_price
                amount += temp
                total_amount = amount + shipping_amount
    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))

    context = {
        'carts': carts,
        'total_amount': total_amount,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_cart': total_cart
    }
    return render(request, 'app/addtocart.html', context)


def plus_cart(request):
    if request.method == 'GET':
        id = request.GET['id']
        c = Cart.objects.get(Q(product=id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp = p.quantity * p.product.discount_price
                amount += temp
                total_amount = amount + shipping_amount
    context = {
        'quantity': c.quantity,
        'amount': amount,
        'total_amount': total_amount

    }
    return JsonResponse(context)


def minus_cart(request):
    if request.method == 'GET':
        id = request.GET['id']
        c = Cart.objects.get(Q(product=id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp = p.quantity * p.product.discount_price
                amount += temp
                total_amount = amount + shipping_amount
    context = {
        'quantity': c.quantity,
        'amount': amount,
        'total_amount': total_amount

    }
    return JsonResponse(context)


@login_required()
def remove_cart(request):
    if request.method == 'GET':
        id = request.GET['id']
        c = Cart.objects.get(Q(product=id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp = p.quantity * p.product.discount_price
                amount += temp

    context = {
        'amount': amount,
        'total_amount': amount + shipping_amount
    }
    return JsonResponse(context)


def mobile(request, data=None):
    total_cart = 0
    mobiles = Product.objects.filter(category='M')
    if data is None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Samsung' or data == 'Nokia' or data == 'Apple' or data == 'Sony' or data == 'Infinix' or data == 'Realme' or data == 'Huawei' or data == 'Vivo' or data == 'Oppo':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discount_price__lt=20000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discount_price__gt=20000)

    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {
        'mobiles': mobiles,
        'total_cart':total_cart
    }

    return render(request, 'app/mobile.html', context)


def laptop(request, data=None):
    total_cart = 0
    laptops = Product.objects.filter(category='L')
    if data is None:
        laptops = Product.objects.filter(category='L')
    elif data == 'Apple' or data == 'Hp' or data == 'Asus' or data == 'Acer' or data == 'Dell' or data == 'Lenovo' or data == 'Msi' or data == 'Gigabyte' or data == 'Sony':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(category='L').filter(discount_price__lt=50000)
    elif data == 'above':
        laptops = Product.objects.filter(category='L').filter(discount_price__gt=50000)

    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {
        'laptops': laptops,
        'total_cart':total_cart
    }
    return render(request, 'app/laptop.html', context)


def Topwear(request, data=None):
    total_cart = 0
    topwears = Product.objects.filter(category='TW')
    if data is None:
        topwears = Product.objects.filter(category='TW')
    elif data == 'below':
        topwears = Product.objects.filter(category='TW').filter(discount_price__lt=500)
    elif data == 'between_500_to_1000':
        topwears = Product.objects.filter(category='TW').filter(discount_price__gt=500, discount_price__lt=1000)
    elif data == 'between_1000_to_2000':
        topwears = Product.objects.filter(category='TW').filter(discount_price__gt=1000, discount_price__lt=2000)
    elif data == 'above':
        topwears = Product.objects.filter(category='TW').filter(discount_price__gt=2000)

    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {
        'topwears': topwears,
        'total_cart':total_cart
    }
    return render(request, 'app/top_wear.html', context)


def BottomWear(request, data=None):
    total_cart = 0
    bottomwears = Product.objects.filter(category='BW')
    if data is None:
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'below':
        bottomwears = Product.objects.filter(category='BW').filter(discount_price__lt=500)
    elif data == 'between_500_to_1000':
        bottomwears = Product.objects.filter(category='BW').filter(discount_price__gt=500, discount_price__lt=1000)
    elif data == 'between_1000_to_2000':
        bottomwears = Product.objects.filter(category='BW').filter(discount_price__gt=1000, discount_price__lt=2000)
    elif data == 'above':
        bottomwears = Product.objects.filter(category='BW').filter(discount_price__gt=2000)

    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {
        'bottomwears': bottomwears,
        'total_cart':total_cart
    }
    return render(request, 'app/bottom_wear.html', context)


def customerregistration(request):
    form = CustomerRegistrationForm()
    if request.method == 'GET':
        form = CustomerRegistrationForm()
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! Registration Successfully!')
    context = {'form': form}
    return render(request, 'app/customerregistration.html', context)


@login_required()
def profile(request):
    total_cart = 0
    form = CustomerProfileForm()
    if request.method == 'GET':
        form = CustomerProfileForm()
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            division = form.cleaned_data['division']
            district = form.cleaned_data['district']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, division=division, district=district,
                           zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!Profile Update Successfully!')

    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {
        'form': form,
        'active': 'btn-primary',
        'total_cart':total_cart
    }
    return render(request, 'app/profile.html', context)


@login_required()
def address(request):
    total_cart = 0
    addr = Customer.objects.filter(user=request.user)
    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {'addr': addr,'total_cart':total_cart}
    return render(request, 'app/address.html', context)


@login_required()
def checkout(request):
    total_cart = 0
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 100.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            temp = p.quantity * p.product.discount_price
            amount += temp
            total_amount = amount + shipping_amount

    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {
        'add': add,
        'cart_items': cart_items,
        'total_amount': total_amount,
        'total_cart': total_cart,
    }
    return render(request, 'app/checkout.html', context)


@login_required()
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect('orders')


@login_required()
def orders(request):
    total_cart = 0
    user = request.user
    odp = OrderPlaced.objects.filter(user=user)

    if request.user.is_authenticated:
        total_cart += len(Cart.objects.filter(user=request.user))
    context = {'odp': odp,'total_cart': total_cart}
    return render(request, 'app/orders.html', context)


def search_item(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(Q(title__icontains=query) | Q(selling_price__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query) | Q(category__icontains=query))
            return render(request,'app/search.html',{'products':products})
        else:
            return render(request,'app/search.html',{'message':'Sorry!! No Match!'})