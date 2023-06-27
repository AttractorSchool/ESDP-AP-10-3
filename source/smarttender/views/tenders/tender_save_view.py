import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from smarttender.models import TrdBuy, Lot, RefTradeMethod, RefUnit, Plan, RefSubjectType, \
    RefBuyStatus, RefTypeTrade


def trd_buy_save(trd_buy):
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


def lot_save(trd_buy, lot):
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


def plan_save(lot, plan):
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


@csrf_exempt
def tender_save_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_tenders = data.get('selectedTenders', [])

            for tender in selected_tenders:
                trd_buy = trd_buy_save(tender)

                lots = tender.get('Lots')
                if lots:
                    for lot in lots:
                        lot_id = lot_save(trd_buy, lot)

                        plans = lot.get('Plans')
                        if plans:
                            for plan in plans:
                                ref_units = plan.get('RefUnits')
                                ref_unit = get_ref_units(ref_units)
                                plan_obj = plan_save(lot_id, plan)
                                plan_obj.ref_units.add(ref_unit)

                trade_methods = tender.get('RefTradeMethods')
                if trade_methods:
                    trade_method = get_ref_trade_methods(trade_methods)
                    trd_buy.ref_trade_methods.add(trade_method)
            # TODO дописать функцию, а именно добавить сохранение остальных полей

            #
            #
            #
            # try:
            #     if not TrdBuy.objects.filter(
            #             number_anno=tender.get('numberAnno'),
            #             name_ru=tender.get('nameRu')
            #     ).exists():
            #         trd_buy = TrdBuy(
            #             number_anno=tender.get('numberAnno'),
            #             name_kz=tender.get('nameKz'),
            #             name_ru=tender.get('nameRu'),
            #             total_sum=tender.get('totalSum'),
            #             count_lots=tender.get('countLots'),
            #             customer_name_kz=tender.get('customerNameKz'),
            #             customer_name_ru=tender.get('customerNameRu'),
            #             org_bin=tender.get('orgBin'),
            #             org_pid=tender.get('orgPid'),
            #             org_name_kz=tender.get('orgNameKz'),
            #             org_name_ru=tender.get('orgNameRu'),
            #             start_date=tender.get('startDate'),
            #             end_date=tender.get('endDate'),
            #             publish_date=tender.get('publishDate'),
            #             itogi_date_public=tender.get('itogiDatePublic')
            #         )
            #         trd_buy.save()
            #
            #         lots = tender.get('Lots')
            #         for lot in lots:
            #             try:
            #                 lot = Lot(
            #                     trd_buy=trd_buy,
            #                     lot_number=lot.get('lotNumber'),
            #                     count=lot.get('count'),
            #                     amount=lot.get('amount'),
            #                     name_kz=lot.get('nameKz'),
            #                     name_ru=lot.get('nameRu'),
            #                     description_kz=lot.get('descriptionKz'),
            #                     description_ru=lot.get('descriptionRu'),
            #                     customer_name_kz=lot.get('customerNameKz'),
            #                     customer_name_ru=lot.get('customerNameRu'),
            #                     dumping=lot.get('dumping')
            #                 )
            #                 lot.save()
            #
            #                 plans = lot.get('Plans')
            #                 for plan in plans:
            #                     try:
            #                         plan = Plan(
            #                             lot=lot,
            #                             subject_name_kz=plan.get('subjectNameKz'),
            #                             subject_name_ru=plan.get('subjectNameRu'),
            #                             name_kz=plan.get('nameKz'),
            #                             name_ru=plan.get('nameRu'),
            #                             count=plan.get('count'),
            #                             price=plan.get('price'),
            #                             amount=plan.get('amount'),
            #                             ref_enstru_code=plan.get('refEnstruCode'),
            #                             desc_kz=plan.get('descKz'),
            #                             desc_ru=plan.get('descRu'),
            #                             supply_date_ru=plan.get('supplyDateRu')
            #                         )
            #                         plan.save()
            #
            #                         ref_units = plans.get('RefUnits')
            #                         for ref_unit in ref_units:
            #                             try:
            #                                 ref_unit = RefUnit(
            #                                     name_kz=ref_unit.get('nameKz'),
            #                                     name_ru=ref_unit.get('nameRu')
            #                                 )
            #                                 ref_unit.save()
            #                             except Exception as ref_unit_err:
            #                                 # Handle RefUnit save error
            #                                 pass
            #                     except Exception as plan_err:
            #                         # Handle Plan save error
            #                         pass
            #             except Exception as lot_err:
            #                 # Handle Lot save error
            #                 pass
            #
            #         trade_methods = tender.get('RefTradeMethods')
            #         for trade_method in trade_methods:
            #             try:
            #                 trade_method = RefTradeMethod(
            #                     name_kz=trade_method.get('nameKz'),
            #                     name_ru=trade_method.get('nameRu'),
            #                     code=trade_method.get('code'),
            #                     symbol_code=trade_method.get('symbolCode')
            #                 )
            #                 trade_method.save()
            #             except Exception as trade_method_err:
            #                 # Handle RefTradeMethod save error
            #                 pass
            #
            #         subject_type = tender.get('RefSubjectType')
            #         try:
            #             subject_type = RefSubjectType(
            #                 name_kz=subject_type.get('nameKz'),
            #                 name_ru=subject_type.get('nameRu')
            #             )
            #             subject_type.save()
            #         except Exception as subject_type_err:
            #             # Handle RefSubjectType save error
            #             pass
            #
            #         buy_status = tender.get('RefBuyStatus')
            #         try:
            #             buy_status = RefBuyStatus(
            #                 name_kz=buy_status.get('nameKz'),
            #                 name_ru=buy_status.get('nameRu'),
            #                 code=buy_status.get('code')
            #             )
            #             buy_status.save()
            #         except Exception as buy_status_err:
            #             # Handle RefBuyStatus save error
            #             pass
            #
            #         type_trade = tender.get('RefTypeTrade')
            #         try:
            #             type_trade = RefTypeTrade(
            #                 name_kz=type_trade.get('nameKz'),
            #                 name_ru=type_trade.get('nameRu')
            #             )
            #             type_trade.save()
            #         except Exception as type_trade_err:
            #             # Handle RefTypeTrade save error
            #             pass
            # except Exception as trd_buy_err:
            #     # Handle TrdBuy save error
            #     pass

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
