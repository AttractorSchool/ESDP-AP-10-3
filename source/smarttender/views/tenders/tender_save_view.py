import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from smarttender.models import TrdBuy, Lot, RefTradeMethod, RefUnit, Plan, RefSubjectType, \
    RefBuyStatus, RefTypeTrade


def create_trd_buy(trd_buy):
    try:
        trd_buy = TrdBuy(
            number_anno=trd_buy.get('numberAnno'),
            name_kz=trd_buy.get('nameKz'),
            name_ru=trd_buy.get('nameRu'),
            total_sum=trd_buy.get('totalSum'),
            count_lots=trd_buy.get('countLots'),
            customer_name_kz=trd_buy.get('customerNameKz'),
            customer_name_ru=trd_buy.get('customerNameRu'),
            org_bin=trd_buy.get('orgBin'),
            org_pid=trd_buy.get('orgPid'),
            org_name_kz=trd_buy.get('orgNameKz'),
            org_name_ru=trd_buy.get('orgNameRu'),
            start_date=trd_buy.get('startDate'),
            end_date=trd_buy.get('endDate'),
            publish_date=trd_buy.get('publishDate'),
            itogi_date_public=trd_buy.get('itogiDatePublic')
        )
        trd_buy.save()
    except KeyError:
        pass
    return trd_buy


def create_lot(trd_buy, lot):
    try:
        lot = Lot(
            trd_buy=trd_buy,
            lot_number=lot.get('lotNumber'),
            count=lot.get('count'),
            amount=lot.get('amount'),
            name_kz=lot.get('nameKz'),
            name_ru=lot.get('nameRu'),
            description_kz=lot.get('descriptionKz'),
            description_ru=lot.get('descriptionRu'),
            customer_name_kz=lot.get('customerNameKz'),
            customer_name_ru=lot.get('customerNameRu'),
            dumping=lot.get('dumping')
        )
        lot.save()
    except KeyError:
        pass
    return lot


def get_ref_units(ref_unit):
    try:
        ref_unit, created = RefUnit.objects.get_or_create(
            name_kz=ref_unit.get('nameKz'),
            name_ru=ref_unit.get('nameRu')
        )
    except KeyError:
        pass
    return ref_unit


def create_plan(lot, plan):
    try:
        plan = Plan(
            lot=lot,
            subject_name_kz=plan.get('subjectNameKz'),
            subject_name_ru=plan.get('subjectNameRu'),
            name_kz=plan.get('nameKz'),
            name_ru=plan.get('nameRu'),
            count=plan.get('count'),
            price=plan.get('price'),
            amount=plan.get('amount'),
            ref_enstru_code=plan.get('refEnstruCode'),
            desc_kz=plan.get('descKz'),
            desc_ru=plan.get('descRu'),
            supply_date_ru=plan.get('supplyDateRu')
        )
        plan.save()
    except KeyError:
        pass
    return plan


def get_ref_trade_methods(trade_methods):
    try:
        ref_trade_method, created = RefTradeMethod.objects.get_or_create(
            name_kz=trade_methods.get('nameKz'),
            name_ru=trade_methods.get('nameRu'),
            code=trade_methods.get('code'),
            symbol_code=trade_methods.get('symbolCode')
        )
        return ref_trade_method
    except KeyError:
        pass


def get_ref_subject_type(subject_type):
    try:
        ref_subject_type, created = RefSubjectType.objects.get_or_create(
            name_kz=subject_type.get('nameKz'),
            name_ru=subject_type.get('nameRu')
        )
        return ref_subject_type
    except KeyError:
        pass


def get_ref_buy_status(buy_status):
    try:
        ref_buy_status, created = RefBuyStatus.objects.get_or_create(
            name_kz=buy_status.get('nameKz'),
            name_ru=buy_status.get('nameRu'),
            code=buy_status.get('code')
        )
        return ref_buy_status
    except KeyError:
        pass


def get_ref_type_trade(type_trade):
    try:
        type_trade, created = RefTypeTrade.objects.get_or_create(
            name_kz=type_trade.get('nameKz'),
            name_ru=type_trade.get('nameRu')
        )
        return type_trade
    except KeyError:
        pass


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
