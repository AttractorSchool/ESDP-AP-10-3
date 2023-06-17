from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from smarttender.models import TrdBuy


def get_cell_data(request):
    cell_id = request.GET.get('cell_id')
    tender = get_object_or_404(TrdBuy, id=cell_id)
    data = {
        'tender_id': tender.id,
        'lot_number': tender.lot.lot_number if tender.lot else None,
        'customer_name_ru': tender.lot.customer_name_ru if tender.lot else None,
        'name_ru': tender.lot.name_ru if tender.lot else None,
        'description_ru': tender.lot.description_ru if tender.lot else None,
        'price': tender.lot.plans.price if tender.lot and tender.lot.plans else None,
        'count': tender.lot.plans.count if tender.lot and tender.lot.plans else None,
        'ref_unit': tender.lot.plans.ref_units.name_ru if tender.lot and tender.lot.plans and tender.lot.plans.ref_units else None,
        'amount': tender.lot.plans.amount if tender.lot and tender.lot.plans else None,
        'supply_date_ru': tender.lot.plans.supply_date_ru if tender.lot and tender.lot.plans else None,
        'products': tender.lot.products.trade_name if tender.lot and tender.lot.products else None,
        'suppliers': tender.lot.suppliers.name if tender.lot and tender.lot.suppliers else None,
        'supplier_discount': tender.supplier_discount,
        'vat': tender.vat,
        'note': tender.note,
        'manager': tender.manager,
        'purchase_price': tender.purchase_price,
        'overall_info': tender.overall_info,
        'publish_date': tender.lot.trd_buy.publish_date if tender.lot and tender.lot.trd_buy else None,
        'end_date': tender.lot.trd_buy.end_date if tender.lot and tender.lot.trd_buy else None,
        'ref_trade_method': tender.lot.trd_buy.ref_trade_methods.name_ru if tender.lot and tender.lot.trd_buy and tender.lot.trd_buy.ref_trade_methods else None,
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
        'commercial_offer_text': tender.commercial_offer_text,
        'status': tender.status
    }
    return JsonResponse(data)
