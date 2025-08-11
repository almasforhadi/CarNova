
from django.urls import path
from . import views

urlpatterns = [
    path('account/signup/', views.Signup, name='signup'),
    path('account/login/', views.Login, name='login'),
    path('account/profile/', views.profile , name='profile'),
    path('account/logout/', views.user_logout , name='logout'),

    path('account/profile/edit_profile/<int:id>', views.edit_profile , name='edit_profile'),
    path('account/profile/edit_profile/change_pass/', views.change_pass , name='change_pass'),
]
