from django.urls import path
from listing import views

app_name = 'listing'
urlpatterns = [
    path('propertylist',views.PropertyListView.as_view(),name='propertylist'),
    path('propertydetail/<int:pk>',views.PropertyDetailView.as_view(),name='propertydetail'),
]