from django.shortcuts import render,redirect
from django.views import View
from listing.forms import AddPropertyForm
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

class PropertyForSaleView(View):
    def get(self, request):
        ps=Property.objects.all()
        context = {'property': ps}
        return render(request, 'propertyforsale.html',context)

class PropertyForRentView(View):
    def get(self, request):
        ps = Property.objects.all()
        context = {'property': ps}
        return render(request, 'propertyforrent.html',context)

class HouseForSaleView(View):
    def get(self, request):
        ps = Property.objects.all()
        context = {'property': ps}
        return render(request, 'houseforsale.html',context)

class FlatForSaleView(View):
    def get(self, request):
        ps = Property.objects.all()
        context = {'property': ps}
        return render(request, 'flatforsale.html',context)

class PlotForSaleView(View):
    def get(self, request):
        ps = Property.objects.all()
        context = {'property': ps}
        return render(request, 'plotforsale.html',context)

class HouseForRentView(View):
    def get(self, request):
        ps = Property.objects.all()
        context = {'property': ps}
        return render(request, 'houseforrent.html',context)

class FlatForRentView(View):
    def get(self, request):
        ps = Property.objects.all()
        context = {'property': ps}
        return render(request, 'flatforrent.html',context)

class PlotForRentView(View):
    def get(self, request):
        ps = Property.objects.all()
        context = {'property': ps}
        return render(request, 'plotforrent.html',context)

class AddPropertyView(View):
    def get(self, request):
        form_instance = AddPropertyForm()
        context = {'form': form_instance}
        return render(request,'addproperty.html',context)
    def post(self, request):
        form_instance = AddPropertyForm(request.POST,request.FILES)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            form_instance.save()
            return redirect('listing:addproperty')

class EditPropertyView(View):
    def get(self, request,i):
        p=Property.objects.get(id=i)
        form_instance = AddPropertyForm(instance=p)
        context = {'form': form_instance}
        return render(request,'editproperty.html',context)
    def post(self, request,i):
        p=Property.objects.get(id=i)
        form_instance = AddPropertyForm(request.POST,instance=p)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('index')

class DeletePropertyView(View):
    def get(self, request,i):
        p=Property.objects.get(id=i)
        p.delete()
        return redirect('index')