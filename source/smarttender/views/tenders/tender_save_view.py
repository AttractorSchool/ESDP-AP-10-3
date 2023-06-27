import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from smarttender.models import TrdBuy
from smarttender.utils.tenders import create_trd_buy, create_lot, get_ref_units, create_plan, get_ref_trade_methods, \
    get_ref_subject_type, get_ref_buy_status, get_ref_type_trade, create_calculation


@csrf_exempt
def tender_save_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_tenders = data.get('selectedTenders', [])

            for tender in selected_tenders:
                if not TrdBuy.objects.filter(
                        number_anno=tender.get('numberAnno'),
                        name_ru=tender.get('nameRu')
                ).exists():
                    trd_buy = create_trd_buy(tender)

                    lots = tender.get('Lots')
                    if lots:
                        for lot in lots:
                            lot_id = create_lot(trd_buy, lot)
                            create_calculation(lot_id)

                            plans = lot.get('Plans')
                            if plans:
                                for plan in plans:
                                    ref_units = plan.get('RefUnits')
                                    ref_unit = get_ref_units(ref_units)
                                    plan_obj = create_plan(lot_id, plan)
                                    plan_obj.ref_units.add(ref_unit)

                    trade_methods = tender.get('RefTradeMethods')
                    if trade_methods:
                        ref_trade_method = get_ref_trade_methods(trade_methods)
                        trd_buy.ref_trade_methods.add(ref_trade_method)

                    subject_type = tender.get('RefSubjectType')
                    if subject_type:
                        ref_subject_type = get_ref_subject_type(subject_type)
                        trd_buy.ref_subject_type.add(ref_subject_type)

                    buy_status = tender.get('RefBuyStatus')
                    if buy_status:
                        ref_buy_status = get_ref_buy_status(buy_status)
                        trd_buy.ref_buy_status.add(ref_buy_status)

                    type_trade = tender.get('RefTypeTrade')
                    if type_trade:
                        ref_type_trade = get_ref_type_trade(type_trade)
                        trd_buy.ref_type_trade.add(ref_type_trade)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
