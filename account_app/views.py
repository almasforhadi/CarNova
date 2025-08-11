from django.shortcuts import render, redirect
from .forms import SingupForm , User, EditForm
from .models import UserProfileModel , PurchaseModel
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def Signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = SingupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = SingupForm()
        return render(request,'signup.html',{'form' : form})
    else:
        return redirect('profile')


def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = AuthenticationForm(request=request , data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = username , password=userpass)
                if user is not None:
                    login(request,user)
                    messages.info(request,'You have successfully logged in!')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form' : form})
    else:
        return redirect('profile')



@login_required
def profile(request):
    # Get all purchase entries for the user
    user_purchases = PurchaseModel.objects.filter(user=request.user)

    # Count how many times each car was purchased
    car_count_dict = {}
    for purchase in user_purchases:
        car = purchase.car
        if car in car_count_dict:
            car_count_dict[car] += 1
        else:
            car_count_dict[car] = 1

    # Prepare list of (car, count) pairs
    car_list = [(car, count) for car, count in car_count_dict.items()]

    return render(request, 'profile.html', {
                                             'car_list': car_list,
                                             'total_unique': len(car_list),  # total different car models purchased
                                            })


@login_required   
def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def edit_profile(request,id):
    item = User.objects.get(pk=id)   # specific id dara model take dorlam

    if request.user != item:         # চেক করো, Logged-in ইউজার কি নিজের প্রোফাইল এডিট করছে
        return redirect('profile')   # অন্য ইউজার প্রোফাইল এডিট করলে তাকে প্রোফাইলে পাঠিয়ে দাও
    
    form = EditForm(instance = item)
    if request.method == 'POST':
        form = EditForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            form = EditForm(instance= item)  # Pre-fill the form with the current user data
    return render(request,'edit_profile.html',{'form':form})



@login_required
def change_pass(request):
     if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, "Password changed successfully.")
            return redirect('edit_profile', id=request.user.id)           # ✅ fix
     else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'change_pass.html',{'form':form})
