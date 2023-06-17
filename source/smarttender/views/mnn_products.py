from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from smarttender.models import TrdBuy, Product, Lot


def similar_products(request, tender_id):
    tender = get_object_or_404(TrdBuy, id=tender_id)
    name_ru_parts = tender.lot.name_ru.split(",")
    query = Q()
    for part in name_ru_parts:
        query |= Q(trade_name__icontains=part.strip()) | Q(ign__icontains=part.strip())

    similar_products = Product.objects.filter(query)
    print(similar_products)
    product_list = []
    for product in similar_products:
        product_data = {
            'id': product.id,
            'trade_name': product.trade_name,
            'producer': product.producer,
            'country': product.country,
            'register_date': product.register_date,
        }
        product_list.append(product_data)

    selected_product_key = f'selected_product_{tender_id}'
    selected_product = request.session.get(selected_product_key)
    context = {
        'tender': tender,
        'product_list': product_list,
        'selected_product': selected_product,
    }
    return render(request, 'modal_product.html', context)


def selected_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('selected_product')
        tender_id = request.POST.get('tender_id')
        action = request.POST.get('action')

        product = get_object_or_404(Product, id=product_id)

        selected_product_key = f'selected_product_{tender_id}'
        selected_product = {
            'id': product.id,
            'trade_name': product.trade_name,
            'producer': product.producer,
            'country': product.country,
            'register_date': product.register_date.strftime('%Y-%m-%d') if product.register_date else 'Нет данных',
        }

        if action == 'choose':
            request.session[selected_product_key] = selected_product
            return redirect('similar_products', tender_id=tender_id)
        elif action == 'save':
            lot = get_object_or_404(Lot, id=tender_id)
            lot.products = product
            lot.save()

            return render(request, 'close_window.html')

    else:
        return JsonResponse({'error': 'Invalid request method.'})
