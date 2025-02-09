from os import stat
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from app_home.views import ResetPasswordView
 # Ensure your view is imported correctly


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutPage,name ="logout"),
    path('register/', views.register, name='register'),
    path('products', views.products, name='products'),
    path('edit-product/<int:id>', views.edit_product, name='edit-product'),
    path('delete-product/<int:id>', views.delete_product, name='delete-product'),
    path('orders', views.orders, name='orders'),
    path('order-new', views.create_order, name='order-new'),
    path('users', views.users, name='users'),
    path('users/user-edit/<int:id>', views.user_edit, name='user-edit'),
    path('user-delete/<int:id>', views.userDelete, name='user-delete'),
    path('user-new', views.create_user, name='user-new'),
    path('products-new', views.create_product, name='products-new'),
    path('app/shopHome/', views.app_home, name="app/shopHome"),
    path('app/home/', views.app_home, name="app/home"),
    path('cart/', views.cart, name ="cart"),
    path('detail/', views.detail, name='detail'),
    path('search/', views.search, name ="search"),
    path('category/', views.category , name ="category"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('settings-account/<int:id>', views.accountEdit,name ="settings-account"),
    path('deactivate-account/', views.deactivate_account, name='deactivate-account'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'), # type: ignore

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

] 