from django.urls import path
from users import views

urlpatterns = [
    path('my_bookings/',views.MyBookingsView.as_view(),name='my-bookings'),
    path('my_bookings/cancel_booking/<int:pk>/',views.BookingCancelView.as_view(),name='cancel-booking')
]
