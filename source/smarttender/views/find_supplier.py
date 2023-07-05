
from django.shortcuts import get_object_or_404, render, redirect
from smarttender.models import Calculation, Lot, Supplier, Offer


def find_supplier(request, tender_id, offer_id):
    tender = get_object_or_404(Calculation, id=tender_id)
    print(tender_id)
    offer = get_object_or_404(Offer, id=offer_id)
    print(offer)
    supplier_list = []
    product_name = offer.product.trade_name if offer.product else ""
    if product_name:
        suppliers = Supplier.objects.filter(product_name__icontains=product_name)
        print(product_name)
        for supplier in suppliers:
            print(supplier)
            supplier_data = {
                'id': supplier.id,
                'name': supplier.name,
                'phone': supplier.phone,
                'email': supplier.email,
                'product_name': supplier.product_name,
            }
            supplier_list.append(supplier_data)

    context = {
        'offer': offer,
        'tender': tender,
        'supplier_list': supplier_list,
    }

    return render(request, 'tender_supplier.html', context)


def selected_supplier(request):
    if request.method == 'POST':
        selected_supplier_id = request.POST.get('selected_supplier')
        offer_id = request.POST.get('offer_id')
        print(offer_id)
        calculation_id = request.POST.get('tender_id')
        calculation = get_object_or_404(Calculation, id=calculation_id)
        print(calculation.lot.id)
        action = request.POST.get('action')

        if action == 'save':
            supplier = get_object_or_404(Supplier, id=selected_supplier_id)
            print(supplier.id)
            offer = get_object_or_404(Offer, id=offer_id)
            product = offer.product
            print(product)

            offer.supplier = supplier
            offer.product = product
            offer.save()

            return redirect('find_supplier', tender_id=calculation_id, offer_id=offer_id)
