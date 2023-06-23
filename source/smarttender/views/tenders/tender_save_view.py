import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from smarttender.models import TrdBuy, Lot, RefTradeMethod, RefUnit, Plan, Offer, Calculation


@csrf_exempt
def tender_save_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_tenders = data.get('selectedTenders', [])

            for tender in selected_tenders:
                if not Lot.objects.filter(
                        lot_number=tender.get('lotNumber'),
                        customer_name_ru=tender.get('customerNameRu'),
                        name_ru=tender.get('nameRu')
                ).exists():
                    trade_method = RefTradeMethod.objects.create(
                        name_ru=tender.get('refTradeMethod')
                    )
                    unit_measure = RefUnit.objects.create(
                        name_ru=tender.get('refUnit')
                    )
                    trd_buy = TrdBuy.objects.create(
                        publish_date=tender.get('publishDate'),
                        end_date=tender.get('endDate'),
                        ref_trade_methods=trade_method,
                        number_anno=tender.get('trdBuyNumberAnno')
                    )
                    plan = Plan.objects.create(
                        price=tender.get('price'),
                        count=tender.get('count'),
                        # ref_units=unit_measure,
                        amount=tender.get('amount'),
                        supply_date_ru=tender.get('supplyDateRu')
                    )
                    plan.ref_units.set([unit_measure])
                    lot = Lot.objects.create(
                        lot_number=tender.get('lotNumber'),
                        customer_name_ru=tender.get('customerNameRu'),
                        name_ru=tender.get('nameRu'),
                        description_ru=tender.get('descriptionRu')
                    )
                    lot.plans.set([plan])
                    lot.trd_buy = trd_buy
                    lot.save()
                    offer = Offer.objects.create(
                        lot=lot
                    )
                    calculation = Calculation.objects.create(
                        lot=lot
                    )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
