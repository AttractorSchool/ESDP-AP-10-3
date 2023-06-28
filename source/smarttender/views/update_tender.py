from django.core.exceptions import ValidationError
from django.http import JsonResponse

from smarttender.models import Calculation


def update_tender(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        tender_id = request.POST.get('tender_id')
        supplier_discount = request.POST.get('supplier_discount')
        vat = request.POST.get('vat')
        note = request.POST.get('note')
        purchase_price = request.POST.get('purchase_price')

        tender = Calculation.objects.get(id=tender_id)

        tender.supplier_discount = supplier_discount if supplier_discount else None
        tender.vat = vat if vat else None
        tender.note = note if note else None
        tender.purchase_price = purchase_price if purchase_price else None

        try:
            tender.save()

            updated_data = {
                'supplier_discount': tender.supplier_discount,
                'vat': tender.vat,
                'note': tender.note,
                'purchase_price': tender.purchase_price,
            }
            return JsonResponse(updated_data)
        except ValidationError as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request'})
