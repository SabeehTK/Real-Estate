from django.urls import path
from listing import views

app_name = 'listing'
urlpatterns = [
    path('propertylist',views.PropertyListView.as_view(),name='propertylist'),
    path('propertydetail/<int:pk>',views.PropertyDetailView.as_view(),name='propertydetail'),
    path('propertyforsale',views.PropertyForSaleView.as_view(),name='propertyforsale'),
    path('propertyforrent',views.PropertyForRentView.as_view(),name='propertyforrent'),
    path('houseforsale',views.HouseForSaleView.as_view(),name='houseforsale'),
    path('flatforsale',views.FlatForSaleView.as_view(),name='flatforsale'),
    path('plotforsale',views.PlotForSaleView.as_view(),name='plotforsale'),
    path('houseforrent',views.HouseForRentView.as_view(),name='houseforrent'),
    path('flatforrent',views.FlatForRentView.as_view(),name='flatforrent'),
    path('plotforrent',views.PlotForRentView.as_view(),name='plotforrent'),
    path('addproperty',views.AddPropertyView.as_view(),name='addproperty'),
    path('editproperty/<int:i>',views.EditPropertyView.as_view(),name='editproperty'),
    path('deleteproperty/<int:i>',views.DeletePropertyView.as_view(),name='deleteproperty'),

]