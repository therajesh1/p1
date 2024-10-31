from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# ecommerce/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category
from django.core.mail import send_mail

# ecommerce/views.py




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# views.py
from django.shortcuts import render, redirect
from .models import Product, Category, Customer, Shopkeeper

# views.py
from django.shortcuts import render, redirect
from .models import Product, Category, Customer, Shopkeeper




from django.shortcuts import render
from .models import Product, Customer, Shopkeeper, Category

from django.shortcuts import render
from .models import Product, Category
import random

def home(request):
    # Fetch all products that are not out of stock
    all_products = list(Product.objects.filter(is_out_of_stock=False))

    # Check if there are any products available
    if len(all_products) > 0:
        # Randomly select 9 products
        products = random.sample(all_products, min(9, len(all_products)))  # Ensure no more than available
    else:
        products = []  # No products available

    # Fetch all categories
    categories = Category.objects.all()
    
    # Render the template with the context
    return render(request, 'home.html', {
        'products': products, 
        'categories': categories
    })



# ecommerce/views.py
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .models import Shopkeeper

# eco/views.py



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Shopkeeper, Customer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Shopkeeper, Customer

def register_shopkeeper(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        shop_name = request.POST['shop_name']
        address = request.POST['address']
        city = request.POST['city']
        phone_number = request.POST['phone_number']
        terms_accepted = request.POST.get('terms_accepted')  # Check if terms are accepted

        if terms_accepted:  # Ensure the shopkeeper accepts the terms
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
            else:
                # Create user
                user = User.objects.create_user(username=username, password=password)
                # Create shopkeeper instance
                shopkeeper = Shopkeeper(user=user, shop_name=shop_name, address=address, city=city, phone_number=phone_number)
                shopkeeper.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('/login')  # Redirect after registration

    return render(request, 'register_shopkeeper.html')


def register_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        address = request.POST['address']
        city = request.POST['city']
        phone_number = request.POST['phone_number']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
        else:
            # Create user
            user = User.objects.create_user(username=username, password=password)
            # Create customer instance
            customer = Customer(user=user, address=address, city=city, phone_number=phone_number)
            customer.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('/login')  # Redirect after registration

    return render(request, 'register_customer.html')



def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})




from django.shortcuts import redirect, get_object_or_404
from .models import  Product








def signin(request):
    return render(request,'signin.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Shopkeeper

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Shopkeeper, Category

@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')  # Assuming you pass category ID from the template
        price = request.POST.get('price')
        
        # Handle multiple file uploads
        image = request.FILES.get('image')  # For image1
        image2 = request.FILES.get('image2')  # For image2
        image3 = request.FILES.get('image3')  # For image3
        image4 = request.FILES.get('image4')  # For image4
        
        # Create the product instance
        product = Product(
            shopkeeper=Shopkeeper.objects.get(user=request.user),
            name=name,
            description=description,
            category_id=category_id,
            price=price,
            image=image,
            image2=image2,
            image3=image3,
            image4=image4,
            is_out_of_stock=False  # Default value
        )
        product.save()
        return redirect('/add_product')  # Redirect to home or a success page

    # If GET request, render the add product page
    categories = Category.objects.all()  # Fetch categories to display in the template
    return render(request, 'add_product.html', {'categories': categories})




from django.contrib.auth import authenticate, login
from .models import Customer, Shopkeeper


from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Shopkeeper, Customer


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']  # Get the user type from the form
        
        # Check if the user exists in the database
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist.')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user type
                if user_type == 'shopkeeper' and hasattr(user, 'shopkeeper'):
                    return redirect('add_product')  # Redirect to add product page for shopkeepers
                elif user_type == 'customer' and hasattr(user, 'customer'):
                    return redirect('home')  # Redirect to home for customers
                else:
                    messages.error(request, 'User type mismatch. Please select the correct user type.')
            else:
                messages.error(request, 'Incorrect password. Please try again.')

    return render(request, 'login.html')



# from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout



# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib import messages


from django.shortcuts import get_object_or_404, redirect
from .models import Product, Shopkeeper
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def manage_products(request):
    # Check if the user is a shopkeeper
    if not hasattr(request.user, 'shopkeeper'):
        return redirect('error_page')  # Redirect customers or unauthorized users

    # Get the shopkeeper instance
    # shopkeeper = request.user.shopkeeper
    try:
        shopkeeper = Shopkeeper.objects.get(user=request.user)
    except Shopkeeper.DoesNotExist:
        return redirect('error_page')  # Redirect if the user is not a shopkeeper
    # Fetch the products for the shopkeeper
    products = Product.objects.filter(shopkeeper=shopkeeper)

    return render(request, 'manage_products.html', {'products': products})

@login_required
def delete_product(request, product_id):
    # Get the product instance or 404 if not found
    product = get_object_or_404(Product, id=product_id)

    # Ensure the product belongs to the logged-in shopkeeper
    if product.shopkeeper != request.user.shopkeeper:
        return redirect('error_page')  # Redirect if the shopkeeper does not own the product

    product.delete()  # Delete the product
    return redirect('manage_products')  # Redirect back to manage products

@login_required
def toggle_stock_status(request, product_id):
    # Get the product instance or 404 if not found
    product = get_object_or_404(Product, id=product_id)

    # Ensure the product belongs to the logged-in shopkeeper
    if product.shopkeeper != request.user.shopkeeper:
        return redirect('error_page')  # Redirect if the shopkeeper does not own the product

    # Toggle the stock status
    product.is_out_of_stock = not product.is_out_of_stock
    product.save()  # Save the product with the new stock status

    return redirect('manage_products')  # Redirect back to manage products




from django.shortcuts import render
from django.views import View  # Import the View class
from .models import Product  # Assuming you have a Product model

class SofaView(View):
    def get(self, request):
        products = Product.objects.filter(category__name='Sofa')  # Filter products by category
        return render(request, 'sofa.html', {'products': products})

class BedView(View):
    def get(self, request):
        products = Product.objects.filter(category__name='Bed')  # Filter products by category
        return render(request, 'bed.html', {'products': products})

# class TableView(View):
#     def get(self, request):
#         products = Product.objects.filter(category='Table')  # Filter products by category
#         return render(request, 'table.html', {'products': products})
class TableView(View):
    def get(self, request):
        products = Product.objects.filter(category__name='Table')  # Ensure 'Table' matches the Category name
        return render(request, 'table.html', {'products': products})


class ChairView(View):
    def get(self, request):
        products = Product.objects.filter(category__name='Chair')  # Filter products by category
        return render(request, 'chair.html', {'products': products})

class CupboardView(View):
    def get(self, request):
        products = Product.objects.filter(category__name='Cupboard')  # Filter products by category
        return render(request, 'cupboard.html', {'products': products})


from django.shortcuts import render, redirect
from p2.models import Product, Order
from django.contrib import messages

def checkout(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        # Create an order
        order = Order.objects.create(
            customer=request.user.customer,
            product=product,
            address=address,
            phone_number=phone_number,
            email=email
        )
        messages.success(request, 'Order placed successfully!')
        return redirect('order_summary', order_id=order.id)

    return render(request, 'checkout.html', {'product': product})

def order_summary(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_summary.html', {'order': order})

def process_payment(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_paid = True  # Update status to paid
    order.save()
    messages.success(request, 'Payment successful!')
    return redirect('order_summary', order_id=order.id)

def customer_orders(request):
    orders = Order.objects.filter(customer=request.user.customer)
    return render(request, 'customer_orders.html', {'orders': orders})

def shopkeeper_orders(request):
    shopkeeper = request.user.shopkeeper
    orders = Order.objects.filter(product__shopkeeper=shopkeeper)
    return render(request, 'shopkeeper_orders.html', {'orders': orders})
