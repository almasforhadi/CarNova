from django.shortcuts import render,redirect , get_object_or_404
from brand_app.models import BrandModel
from car_app.models import CarModel
from account_app.models import CommentModel , UserProfileModel , PurchaseModel
from account_app.forms import CommentForm
from django.contrib.auth.decorators import login_required


def home(request, brand_slug = None):
    brands = BrandModel.objects.all()
    cars = CarModel.objects.all()

    filtered_car = None
    if brand_slug:
         brand = BrandModel.objects.get(slug = brand_slug)
         filtered_car = CarModel.objects.filter(brand = brand)
    
    return render(request,'home.html',{
                                         "brands": brands,
                                         'filtered_car': filtered_car,
                                         'all_cars':cars,
                                      })


def view_details(request,id):
     car_item = CarModel.objects.get(pk=id)
     comments = CommentModel.objects.all()
     
     # Count total purchases of this car
     purchase_count = PurchaseModel.objects.filter(car=car_item).count()

     if request.method == 'POST':
          form = CommentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('view_details', id=id)
     else:
          form = CommentForm()
     return render(request,'view_details.html',{
                                                 'form': form ,
                                                 'car_item': car_item,
                                                 'comments':comments,
                                                 'purchase_count': purchase_count
                                               })


@login_required
def buy_car(request, id):
    car_item = get_object_or_404(CarModel, pk=id)
    # user_profile, _ = UserProfileModel.objects.get_or_create(user=request.user)

    if car_item.car_quantity > 0:
        car_item.car_quantity -= 1
        car_item.save()

        #Just save the purchase, no need to use purchased_cars
        PurchaseModel.objects.create(user=request.user, car=car_item)

        return redirect('profile')
    else:
        return render(request, 'view_details.html', {
            'car_item': car_item,
            'message': 'This car is out of stock.'
        })

     
