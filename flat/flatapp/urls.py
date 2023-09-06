from django.urls import path
from flatapp import views

urlpatterns = [
    path('',views.index),
    path('register/',views.register),
    path('bookflat/',views.bookflat),
    path('showbooking/',views.showflats),
    path('delete/<rid>',views.deleteflats),
    path('edit/<rid>',views.updateflats),
    path('mumbai',views.mumbai),
    path('bangalore',views.bangalore),
    path('pune',views.pune),
    path('delhi',views.delhi),
    path('residency',views.residency),
    path('registration/',views.registration),
    path('login/',views.login),
    path('about',views.about),
    path('contact/',views.addcontact),
    path('contactus/',views.addcontactus),
    path('showcontact/',views.showcontact),
]