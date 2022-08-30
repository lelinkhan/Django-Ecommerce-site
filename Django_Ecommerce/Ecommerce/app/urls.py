from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyChangePasswordForm,MyPasswordResetForm, MyPasswordSetForm

urlpatterns = [
    path('', views.home, name='home'),
    path('product-detail/<int:pk>/', views.product_detail, name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('add-to-cart/<int:pk>', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),

    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),

    path('search/',views.search_item, name='search'),

    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>/', views.laptop, name='laptopdata'),

    path('topwear/', views.Topwear, name='topwear'),
    path('topwear/<slug:data>/', views.Topwear, name='topwearData'),

    path('bottomwear/', views.BottomWear, name='bottomwear'),
    path('bottomwear/<slug:data>/', views.BottomWear, name='bottomwearData'),

    path('registration/', views.customerregistration, name='customerregistration'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyChangePasswordForm, success_url= '/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name = 'app/passwordchangedone.html'), name='passwordchangedone'),


    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=MyPasswordSetForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
]
