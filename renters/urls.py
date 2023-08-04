from django.urls import path
from renters import views

urlpatterns = [
    path('home',views.home,name='renters-home'),
    path('register/',views.RenterRegisterView.as_view(),name='renter-register-profile'),
    path('my-vehicles/',views.RenterVehicleListView.as_view(),name='renter-vehicle-list'),
    path('view_bookings/<int:pk>/',views.ViewBookingsView.as_view(),name='view-bookings'),
    path('cancel_booking/<int:pk>',views.CancelBookingView.as_view(),name='cancel-booking-renter'),
    path('my_bookings/',views.MyBookingsRenterView.as_view(), name='my-bookings-renter'),

]
