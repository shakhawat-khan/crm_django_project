from django.conf.urls import url
from . import views
from django.urls import path 

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home" ),
    path('product/', views.products_url, name='product' ) ,
    path('customer/<str:obj_id>/', views.customer_url,name="customer" ) , # here obj_id is number of the pertucal object for a url
    path('create_order/',views.createorder,name='create_order' ),
    path('create_customer/' ,views.createcustomer,name='create_customer'),
    path('update_order/<str:obj_id>',views.updateorder ,name='update_order'),
    path('delete_order/<str:obj_id>',views.deleteorder ,name='delete_order'), #name is for dymanic url routing.
    path('login/',views.loginpage ,name='login'),
    path('register/',views.register ,name='register'),
    path('logout/',views.logoutUser ,name='logout'),
    path('userpage/',views.userPage ,name='userpage'),
    path('account/',views.accountSettings ,name='account'),
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),



]



'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''


