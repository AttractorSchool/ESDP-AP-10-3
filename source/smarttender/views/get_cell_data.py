from array import array

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from smarttender.models import Calculation, Plan, TrdBuy, Offer, RefUnit


def get_cell_data(request):
    cell_id = request.GET.get('cell_id')
    tender = get_object_or_404(Calculation, id=cell_id)
    plan = get_object_or_404(Plan, lot=tender.lot)
    offer = get_object_or_404(Offer, lot=tender.lot)
    data = {
        'tender_id': tender.id,
        'lot_number': tender.lot.lot_number,
        'customer_name_ru': tender.lot.customer_name_ru,
        'name_ru': tender.lot.name_ru,
        'description_ru': tender.lot.description_ru,
        'price': plan.price,
        'count': plan.count,
        'ref_unit':  list(plan.ref_units.values('name_ru')),
        'amount': plan.amount,
        'supply_date_ru': plan.supply_date_ru,
        'products': offer.product.trade_name,
        'suppliers': offer.supplier.name,
        'supplier_discount': tender.supplier_discount,
        'vat': tender.vat,
        'note': tender.note,
        'manager': tender.manager,
        'purchase_price': tender.purchase_price,
        'overall_info': tender.overall_info,
        'publish_date': tender.lot.trd_buy.name_ru,
        'end_date': tender.lot.trd_buy.end_date,
        'ref_trade_method': tender.lot.trd_buy.ref_trade_methods.first().name_ru,
        'paper_ad_link': tender.paper_ad_link,
        'lot_link': tender.lot_link,
        'profit_rate': tender.profit_rate,
        'delivery_rate': tender.delivery_rate,
        'purchase_price_per_unit': tender.purchase_price_per_unit,
        'bidding_price_per_unit': tender.bidding_price_per_unit,
        'budget_price_per_unit': tender.budget_price_per_unit,
        'overall_profit': tender.overall_profit,
        'overall_purchase_amount': tender.overall_purchase_amount,
        'overall_contract_amount': tender.overall_contract_amount,
        'winning_price': tender.winning_price,
        'commercial_offer_text': tender.commercial_offer_text
        # 'status': tender.status
    }
    return JsonResponse(data)
