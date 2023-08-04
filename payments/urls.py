from django.urls import path

from payments import views

urlpatterns = [
 path('<int:pk>/book/',views.BookingView.as_view(),name='vehicle-booking')   
]
