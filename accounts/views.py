from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from .models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render
from products.models import Product


class AccountRegistration(CreateView):
    template_name = "accounts/registration.html"
    form_class = CustomUserCreationForm
    model = User
    success_url = reverse_lazy("accounts:register-success")


class AccountRegistrationSuccess(TemplateView):
    template_name = "accounts/registration_success.html"


class AccountLogin(LoginView):
    template_name = "accounts/login.html"


class AccountLogout(LogoutView):
    next_page = reverse_lazy("products:list")


def list(request):
    users = User.objects.all()
    return render(request, 'accounts/accounts.html', {'users':users})


def profile(request, username):
    userProfile = User.objects.get(username=username)

    data = {
        "accounts": userProfile,
    }
    return render(request, "accounts/profile.html", data)


def follow(request, username):
    accountsObj = User.objects.get(username=username)
    currentUserObj = User.objects.get(username=request.user.username)
    following = accountsObj.following.all()

    if username != currentUserObj.username:
        if currentUserObj in following:
            accountsObj.following.remove(currentUserObj.id)
        else:
            accountsObj.following.add(currentUserObj.id)

    return HttpResponseRedirect(reverse('accounts:profile', args=[accountsObj.username]))


def viewed(request, product_id):
    accountsObj = User.objects.get(username=request.user.username)
    productObj = Product.objects.get(pk=product_id)
    viewed = accountsObj.viewed.all()

    if productObj not in viewed:
        accountsObj.viewed.add(productObj.id)

    return None


def recommendations(request):
    currentUserObj = User.objects.get(username=request.user.username)
    following = currentUserObj.following.all()
    max_product_recommendation = 10
    recommended_products = []
    count = 0
    for follower in following:
        viewed = follower.viewed.all()
        for product in viewed:
            productObj = Product.objects.get(pk=product.id)
            recommended_products.append(productObj)
            count+=1
        if count == max_product_recommendation:
            break
    return render(request, "products/list.html", {"page_obj":recommended_products})

# 26, 70, 100