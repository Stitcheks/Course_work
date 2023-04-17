from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from main.models import Catalog
from main.models import Brand
from orders.models import Order
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from cart.cart import Cart
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,
                                  'registration/authenticated_successfully.html',
                                  context={'user': user})
                else:
                    return HttpResponse('Аутентификация не удалась')
            else:
                return HttpResponse('Неправильный логин')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', context={'form': form})


def user_logout(request):
    cats = Catalog.objects.all()
    brands = Brand.objects.all()
    logout(request)
    return render(request, 'main/main_page.html', context={'cats': cats, 'brands': brands})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(
                request,
                'registration/register_done.html',
                context={'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', context={'user_form': user_form})


@login_required
def edit(request):
    orders = Order.objects.filter(user_id=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', context={'user_form': user_form,
                                                         'profile_form': profile_form,
                                                         'orders': orders,
                                                         })
