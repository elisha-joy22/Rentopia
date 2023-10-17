from django.urls import path,include
from vehicle import views


urlpatterns = [
    path('serializer/',views.VehicleSerializerView.as_view(),name='serializer'),
    path('',views.VehicleListView.as_view(),name='vehicle-types-list'),
    path('my-vehicles/',views.VehicleCredentialListView.as_view(),name='vehicle-list'),
    path('<int:pk>/info',views.VehicleCredentialDetailView.as_view(),name='vehicle-detail'),
    path('<int:pk>/delete',views.VehicleDeleteView.as_view(),name='vehicle-delete'),
    path('download/pdf/<str:kl_number>/<str:pdf_type>',views.download_documents_pdf,name='vehicle-document-download'),
    path('add-vehicle-credential/form',views.VehicleCredentialView.as_view(),name='add-vehicle-credential')
]
