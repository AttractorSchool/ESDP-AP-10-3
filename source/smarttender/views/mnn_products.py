from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from smarttender.models import Calculation, Product, Lot, Offer


def similar_products(request, calculation_id):
    calculation = get_object_or_404(Calculation, id=calculation_id)
    name_ru_parts = calculation.lot.name_ru.split(",")
    query = Q()
    for part in name_ru_parts:
        query |= Q(trade_name__icontains=part.strip()) | Q(ign__icontains=part.strip())

    similar_products = Product.objects.filter(query)
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

    selected_products_key = f'selected_products_{calculation_id}'
    if request.method == 'POST':
        selected_products = request.POST.getlist('selected_products')
        request.session[selected_products_key] = selected_products
    else:
        selected_products = request.session.get(selected_products_key, [])

    context = {
        'tender': calculation,
        'product_list': product_list,
        'selected_products': selected_products,
    }

    return render(request, 'modal_product.html', context)


def selected_product(request):
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_product')
        calculation_id = request.POST.get('tender_id')
        action = request.POST.get('action')

        selected_products = []
        for product_id in selected_product_ids:
            product = get_object_or_404(Product, id=product_id)
            selected_product = {
                'id': product.id,
                'trade_name': product.trade_name,
                'producer': product.producer,
                'country': product.country,
                'register_date': product.register_date.strftime('%Y-%m-%d') if product.register_date else 'Нет данных',
            }
            selected_products.append(selected_product)

        if action == 'save':
            selected_products_key = f'selected_products_{calculation_id}'
            request.session[selected_products_key] = selected_products
            for product_id in selected_product_ids:
                product = get_object_or_404(Product, id=product_id)
                print(product)
                offer = Offer.objects.create(lot_id=calculation_id, product=product)
            return redirect('similar_products', calculation_id=calculation_id)

    return JsonResponse({'error': 'Invalid request method.'})

