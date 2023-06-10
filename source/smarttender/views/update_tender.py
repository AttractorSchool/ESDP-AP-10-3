from django.core.exceptions import ValidationError
from django.http import JsonResponse

from smarttender.models import Tender


def update_tender(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        tender_id = request.POST.get('tender_id')
        supplier = request.POST.get('supplier')
        price_without_discount = request.POST.get('price_without_discount')
        supplier_discount = request.POST.get('supplier_discount')
        price_with_discount = request.POST.get('price_with_discount')
        vat = request.POST.get('vat')
        note = request.POST.get('note')
        purchase_price = request.POST.get('purchase_price')

        tender = Tender.objects.get(id=tender_id)

        tender.supplier = supplier
        tender.price_without_discount = price_without_discount if price_without_discount else None
        tender.supplier_discount = supplier_discount if supplier_discount else None
        tender.price_with_discount = price_with_discount if price_with_discount else None
        tender.vat = vat if vat else None
        tender.note = note
        tender.purchase_price = purchase_price if purchase_price else None

        try:
            tender.save()

            updated_data = {
                'supplier': tender.supplier,
                'price_without_discount': tender.price_without_discount,
                'supplier_discount': tender.supplier_discount,
                'price_with_discount': tender.price_with_discount,
                'vat': tender.vat,
                'note': tender.note,
                'purchase_price': tender.purchase_price,
            }
            return JsonResponse(updated_data)
        except ValidationError as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request'})
