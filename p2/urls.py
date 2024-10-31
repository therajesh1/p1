# ecommerce/urls.py

from django.urls import path
from p2 import views
from .views import register_shopkeeper, register_customer
from .views import SofaView, BedView, TableView, ChairView, CupboardView



urlpatterns = [
    path('', views.home, name='home'),
    # path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
     # Ensure this is defined
    path('register_shopkeeper/', views.register_shopkeeper, name='register_shopkeeper'),
    path('register_customer/', views.register_customer, name='register_customer'),
    path('signin/', views.signin, name='signin'),
    path('add_product/', views.add_product, name='add_product'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # URL for logout
    path('manage-products/', views.manage_products, name='manage_products'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('toggle-stock-status/<int:product_id>/', views.toggle_stock_status, name='toggle_stock_status'),
    path('sofa/', SofaView.as_view(), name='sofa'),
    path('bed/', BedView.as_view(), name='bed'),
    path('table/', TableView.as_view(), name='table'),
    path('chair/', ChairView.as_view(), name='chair'),
    path('cupboard/', CupboardView.as_view(), name='cupboard'),
        # Product Detail and Buy Now
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    
    # Order Summary and Payment Processing
    # path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'),

    path('process_payment/<int:order_id>/', views.process_payment, name='process_payment'),

    # Customer Orders and Shopkeeper Orders
    path('customer_orders/', views.customer_orders, name='customer_orders'),
    path('shopkeeper_orders/', views.shopkeeper_orders, name='shopkeeper_orders'),
   


]

# urls.py

