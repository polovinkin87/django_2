from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm, CreateCategoryForm, CreateProductForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'пользователи/создать'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form
    }

    return render(request, 'adminapp/user_create.html', context)


def user_update(request, pk):
    title = 'пользователи/редактировать'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    context = {
        'title': title,
        'user_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_deleted = True
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', context)


def category_update(request, pk):
    title = 'создание категории'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        create_cat = CreateCategoryForm(request.POST, request.FILES, instance=category)
        if create_cat.is_valid():
            create_cat.save()
            return HttpResponseRedirect('/adminapp/categories/read/')
    else:
        create_cat = CreateCategoryForm(instance=category)

    context = {'title': title, 'create_cat': create_cat}

    return render(request, 'adminapp/category_create.html', context)


def category_create(request):
    title = 'создание категории'

    if request.method == 'POST':
        create_cat = CreateCategoryForm(request.POST, request.FILES)
        if create_cat.is_valid():
            create_cat.save()
            return HttpResponseRedirect('/adminapp/categories/read/')
    else:
        create_cat = CreateCategoryForm()

    context = {'title': title, 'create_cat': create_cat}

    return render(request, 'adminapp/category_create.html', context)


def category_delete(request, pk):
    title = 'удаление категории'
    category = get_object_or_404(ProductCategory, pk=pk)
    category.delete()
    return HttpResponseRedirect('/adminapp/categories/read/')


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
