from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *
from .forms import *

from .filters import OrderFilter

from django.shortcuts import redirect

from .filters import OrderFilter

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .decorators import unauthenticated_user ,allowed_users,admin_only

#from django.contrib.auth.forms import inlineformset_factory




@unauthenticated_user #this is decorators 

def loginpage(request):

    context = {}

    if request.user.is_authenticated:

        return redirect('home')

    else :
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home') 

            else:
                messages.info(request,'Username OR password is incorrect')
                return render(request,'accounts/login.html',context)      

        context = {}
        
        return render(request,'accounts/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user

def register(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)



@login_required(login_url='login')
#@admin_only
#@allowed_users(allowed_roles=['customer'])
def userPage(request):
    
    #order = customer.user.objects.all()
    #print(order)
    #customerID = customer.objects.filter(user=request.user)
    #customer_orders = order.objects.filter(customer=customerID)
    #print(customer_orders)

    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status= 'Deliverd').count()
    pending = orders.filter(status = 'pending').count()
    
    context = {'order':orders , 'total_order':total_orders ,
    'delivered':delivered,'pending':pending  }
    return render(request,'accounts/user.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

#@admin_only

def home(request):

    orders = order.objects.all()
    cus = customer.objects.all()

    total_customer = cus.count()
    total_order = orders.count()

    delivered = orders.filter(status= 'Deliverd').count()
    pending = orders.filter(status = 'pending').count()

    context = {'order' : orders, 'cus': cus , 'total_customer':total_customer,
    'total_order':total_order,'delivered':delivered,'pending':pending }
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def products_url(request):

    pro = product.objects.all()

    return render(request, 'accounts/products.html' ,{'product' : pro } )



@login_required(login_url='login')


def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    context = {'form' : form}

    if request.method == 'POST':

        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    return render(request,'accounts/account_settings.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def customer_url(request, obj_id):

    cust = customer.objects.get(id=obj_id)

    orders = cust.order_set.all()
    order_count = orders.count()
    
    #cust = customer.objects.get(id=obj_id)

    myFilter = OrderFilter(request.GET,queryset=orders)

    orders = myFilter.qs

    ord = cust.order_set.all()
    ord_count = ord.count()
    context = {'customer':cust ,'orders':orders , 'count' : ord_count,'myFilter':myFilter }
    return render(request, 'accounts/customer.html',context) 


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def createorder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context ={'form':form}

    
    return render(request,'accounts/order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def createcustomer(request):

    form = CustomerForm()

    context = {'form':form}

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'accounts/customer_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def updateorder(request,obj_id):
    ord =order.objects.get(id=obj_id) 
    form = OrderForm(instance=ord)
    
    if request.method == 'POST':
        form=OrderForm(request.POST,instance=ord)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form  }
    return render(request,'accounts/order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def deleteorder(request,obj_id):
    ord =order.objects.get(id=obj_id)

    if request.method=="POST":
        ord.delete()
        return redirect('/')

    context = {'item':ord}
    return render(request, 'accounts/delete.html',context )