from django import forms
from .models import Customer, Service, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'organization', 'role', 'bldgroom', 'account_number', 'address', 'city', 'state', 'zipcode', 'email')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('category','name', 'author', 'image', 'edition', 'price', 'sellername', 'selleremail', 'sellerphone')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('cust_name', 'product', 'p_description', 'quantity', 'pickup_time', 'charge')


class EmailPostForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    Your_email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    Seller_email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))

