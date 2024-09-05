# Create your views here.
# views.py
from django.shortcuts import render
from .models import Drug, Vendor, Hospital, SupplyOrder



def dashboard(request):
    drugs = Drug.objects.all()
    vendors = Vendor.objects.all()
    hospitals = Hospital.objects.all()
    supply_orders = SupplyOrder.objects.all()

    return render(request, 'dashboard.html', {
        'drugs': drugs,
        'vendors': vendors,
        'hospitals': hospitals,
        'supply_orders': supply_orders
    })

def vendor_activity(request, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    supply_orders = SupplyOrder.objects.filter(vendor=vendor)

    return render(request, 'vendor_activity.html', {
        'vendor': vendor,
        'supply_orders': supply_orders
    })

def hospital_activity(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)
    supply_orders = SupplyOrder.objects.filter(hospital=hospital)
    return render(request, 'hospital_activity.html', {'hospital': hospital, 'supply_orders': supply_orders})