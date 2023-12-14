from rest_framework import generics
from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer, Product, Order, OrderItem
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from . forms import OrderItemForm
from django.http import HttpResponseForbidden,HttpResponse
from django.views import View
from .models import Customer
from .forms import CustomerForm,ProductForm,Order
import datetime
from django.contrib.auth import authenticate, login
import random
class CustomerCreateView(View):
    template_name = 'customer_create.html'

    def get(self, request):
        form = CustomerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('customer-list-create')  
        return render(request, self.template_name, {'form': form})
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        customers = self.get_queryset()
        return render(request, 'customer_list.html', {'customers': customers})

class CustomerUpdateView(View):
    template_name = 'customer_update.html'

    def get(self, request, pk=None):
        customer = Customer.objects.get(pk=pk)
        form = CustomerForm(instance=customer)
        return render(request, self.template_name, {'form': form, 'customer': customer})

    def post(self, request, pk=None):
        customer = Customer.objects.get(pk=pk)
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return HttpResponse('Customer updated successfully.')
        return render(request, self.template_name, {'form': form, 'customer': customer})
    
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = self.get_queryset()
        return render(request, 'product_list.html', {'products': products})


class ProductCreateView(View):
    template_name = 'product_create.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('product-list-create')  
        return render(request, self.template_name, {'form': form})

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        orders = self.get_queryset()
        return render(request, 'order_list.html', {'orders': orders})

class OrderCreateView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        
        customer = request.user.customer
        print("=========================",customer,"===================",product_id,"======================")
        order_no = f"ORD{random.randint(100, 999)}"
        order, created = Order.objects.get_or_create(
            customer=customer,
            order_date=datetime.date.today(), 
            address="Pune Maharashtra 411005",
            order_number=order_no

        )
        
        product = Product.objects.get(id=product_id)
        order.products.add(product)
        order.save()
        return redirect('product-list-create')

class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        form = OrderItemForm(instance=order)
        return render(request, 'order_update.html', {'order': order, 'form': form})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        form = OrderItemForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            return render(request, 'order_update.html', {'order': instance, 'form': form})
        else:
            return render(request, 'order_update.html', {'order': instance, 'form': form})

class OrderListByCustomerView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer_name = self.request.query_params.get('customer')
        return Order.objects.filter(customer__name=customer_name)

class OrderListByProductView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        product_names = self.request.query_params.getlist('products')
        print("=========",product_names)
        return Order.objects.filter(order_item__product__name__in=product_names)
class CustomerFormView(View):
    template_name = 'customer_form.html'

    def get(self, request, pk=None):
        if pk:
            customer = get_object_or_404(Customer, pk=pk)
            form = CustomerForm(instance=customer)
        else:
            form = CustomerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk=None):
        if pk:
            customer = get_object_or_404(Customer, pk=pk)
            form = CustomerForm(request.POST, instance=customer)
        else:
            form = CustomerForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse('Customer saved successfully.')
        return render(request, self.template_name, {'form': form})



