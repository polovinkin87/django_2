from django import forms
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm
from django.forms import ModelForm
from mainapp.models import ProductCategory, Product


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class CreateCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', )


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'category',)