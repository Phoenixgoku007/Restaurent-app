from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant
from dish.models import Dish
from review.models import Review
from bookmark.models import Bookmark
from visit.models import Visit
from cuisine.models import Cuisine
from .forms import ReviewForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            context = {'error': 'Invalid login credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    reviews = Review.objects.filter(restaurant=restaurant)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('restaurant_detail', id=id)
    else:
        form = ReviewForm()
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'reviews': reviews, 'form': form})

def restaurant_list_view(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant_list.html', context)

def restaurant_detail_view(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    reviews = Review.objects.filter(restaurant=restaurant).order_by('id')
    dishes = Dish.objects.filter(restaurant=restaurant)
    bookmarked = Bookmark.objects.filter(user=request.user, restaurant_id=id).exists()

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
        'dishes': dishes,
        'bookmarked': bookmarked,
    }

    return render(request, 'restaurant_detail.html', context)




@login_required
def add_review(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('restaurant_detail', id=id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'restaurant': restaurant, 'form': form})


@login_required
def edit_review(request, id):
    review = get_object_or_404(Review, id=id)
    if request.user != review.user:
        messages.error(request, 'You are not authorized to edit this review.')
        return redirect('restaurant_detail', id=review.restaurant.id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully.')
            return redirect('restaurant_detail', id=review.restaurant.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'review': review, 'form': form})


@login_required
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    if request.user != review.user:
        messages.error(request, 'You are not authorized to delete this review.')
        return redirect('restaurant_detail', id=review.restaurant.id)
    review.delete()
    messages.success(request, 'Review deleted successfully.')
    return redirect('restaurant_detail', id=review.restaurant.id)


@login_required
def add_bookmark(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if Bookmark.objects.filter(user=request.user, restaurant=restaurant).exists():
        messages.warning(request, 'Restaurant already bookmarked.')
    else:
        bookmark = Bookmark(user=request.user, restaurant=restaurant)
        bookmark.save()
        messages.success(request, 'Restaurant bookmarked successfully.')
    return redirect('restaurant_detail', id=id)


@login_required
def remove_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    if request.user != bookmark.user:
        messages.error(request, 'You are not authorized to remove this bookmark.')
        return redirect('restaurant_detail', id=bookmark.restaurant.id)
    bookmark.delete()
    messages.success(request, 'Bookmark removed successfully.')
    return redirect('restaurant_detail', id=id)

@login_required
def add_visit(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if Visit.objects.filter(user=request.user, restaurant=restaurant).exists():
        messages.warning(request, 'Restaurant already marked as visited.')
    else:
        visit = Visit(user=request.user, restaurant=restaurant)
        visit.save()
        messages.success(request, 'Restaurant marked as visited successfully.')
    return redirect('restaurant_detail', id=id)


@login_required
def remove_visit(request, id):
    visit = get_object_or_404(Visit, id=id)
    if request.user != visit.user:
        messages.error(request, 'You are not authorized to remove this visit.')
        return redirect('restaurant_detail', id=visit.restaurant.id)
    visit.delete()
    messages.success(request, 'Visit removed successfully.')
    return redirect('restaurant_detail', id=visit.restaurant.id)

@login_required
def add_review_view(request, id):
    restaurant = Restaurant.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            return redirect('restaurant_detail', id=id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'restaurant': restaurant, 'form': form})

@login_required
def edit_review_view(request, id):
    review = get_object_or_404(Review, id=id, user=request.user)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('restaurant_detail', id=review.restaurant.id)
    return render(request, 'edit_review.html', {'form': form, 'review': review})

def delete_review_view(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('restaurant_detail', id=review.restaurant.id)

    context = {'review': review}
    return render(request, 'delete_review.html', context)

@login_required
def add_bookmark_view(request, id):
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, restaurant_id=id)
    if not created:
        bookmark.delete()
    return redirect('restaurant_detail', id=id)


@login_required
def remove_bookmark_view(request, id):
    bookmark = get_object_or_404(Bookmark, user=request.user, restaurant_id=id)
    bookmark.delete()
    return redirect('restaurant_detail', id=id)


@login_required
def add_visit_view(request, id):
    visit, created = Visit.objects.get_or_create(user=request.user, restaurant_id=id)
    if not created:
        visit.delete()
    return redirect('restaurant_detail', id=id)


@login_required
def remove_visit_view(request, id):
    visit = get_object_or_404(Visit, user=request.user, restaurant_id=id)
    visit.delete()
    return redirect('restaurant_detail', id=id)