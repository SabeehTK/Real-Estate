from django.shortcuts import render
from django.views import View

from listing.models import Property


# Create your views here.
class IndexView(View):
    def get(self, request):
        p=Property.objects.all()
        context = {'property_list': p}
        return render(request, 'index.html',context)

class PropertyListView(View):
    def get(self, request):
        p=Property.objects.all()
        context = {'property_list': p}
        return render(request, 'propertylist.html',context)

class PropertyDetailView(View):
    def get(self, request,pk):
        p=Property.objects.get(id=pk)
        context = {'property': p}
        return render(request, 'propertydetail.html',context)