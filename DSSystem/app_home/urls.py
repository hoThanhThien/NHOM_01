from os import stat
from django.urls import path
from . import views
 # Ensure your view is imported correctly


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutPage,name ="logout"),
    #path('auth-register-basic/', views.registerPage, name='register'),
    path('products', views.products, name='products'),
    path('edit-product/<int:id>', views.edit_product, name='edit-product'),
    path('delete-product/<int:id>', views.delete_product, name='delete-product'),
    path('users', views.users, name='users'),
    path('user-edit/<int:id>', views.userEdit, name='user-edit'),
    path('user-delete/<int:id>', views.userDelete, name='user-delete'),
    path('user-new', views.create_user, name='user-new'),
    path('products-new', views.create_product, name='products-new'),
    path('app/home/', views.app_home, name="app/home"),
    path('app/cart/', views.cart, name ="cart"),
    path('detail/', views.detail, name ="detail"),
    path('search/', views.search, name ="search"),
    path('category/', views.category , name ="category"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('register/', views.register,name ="register"),
   
] 