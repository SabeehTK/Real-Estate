from listing.models import Property


def links(request):
    p=Property.objects.all()
    return {'propertylist': p}