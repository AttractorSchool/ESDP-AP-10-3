from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from smarttender.models import Tender


def get_cell_data(request):
    cell_id = request.GET.get('cell_id')
    tender = get_object_or_404(Tender, id=cell_id)
    data = {
        'lot': tender.lot,
        'company': tender.company,
        'name': tender.name,
        'price_per_unit': tender.price_per_unit,
        'quantity': tender.quantity,
        'planned_amount': tender.planned_amount,
        'delivery_deadline': tender.delivery_deadline,
        'proposed_product_name': tender.proposed_product_name,
        'supplier': tender.supplier,
        'price_without_discount': tender.price_without_discount,
        'supplier_discount': tender.supplier_discount,
        'price_with_discount': tender.price_with_discount,
        'vat': tender.vat,
        'note': tender.note,
        'manager': tender.manager,
        'purchase_price': tender.purchase_price,
        'overall_info': tender.overall_info,
        'date': tender.date,
        'deadline': tender.deadline,
        'procurement_type': tender.procurement_type,
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
        'status': tender.status,
    }
    return JsonResponse(data)












