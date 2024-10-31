from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# ecommerce/models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ecommerce/models.py

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Shopkeeper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)  # Address field
    city = models.CharField(max_length=100)  # City field
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()  # Temporarily remove unique=True


    def __str__(self):
        return self.shop_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)  # Address field
    city = models.CharField(max_length=100)  # City field
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username



# models.py


    

from django.db import models

class Product(models.Model):
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # date=models.DateField()

    # Primary image
    image = models.ImageField(upload_to='product_images/')
    # Optional additional images
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    # Status fields
    is_out_of_stock = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)  # New field for sold status

    def __str__(self):
        return f"{self.name} ({'Out of Stock' if self.is_out_of_stock else 'In Stock'}, {'Sold' if self.is_sold else 'Available'})"



from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.product.name} by {self.customer.user.username}"






