from django.shortcuts import render, redirect
from smarttender.models import Tender, Product
from django.http import JsonResponse, HttpResponse


def find_similar_products(request, tender_id):
    tender = Tender.objects.get(id=tender_id)
    similar_products = Product.objects.filter(trade_name__icontains=tender.lot.name_ru)
    product_list = []
    for product in similar_products:
        product_data = {
            'trade_name': product.trade_name,
            'producer': product.producer,
            'country': product.country,
            'register_date': product.register_date,
        }
        product_list.append(product_data)
    data = {
        'tender_id': tender.id,
        'similar_products': product_list,
    }
    return JsonResponse(data)


def similar_products(request, tender_id):
    tender = Tender.objects.get(id=tender_id)
    similar_products = Product.objects.filter(trade_name__icontains=tender.lot.name_ru)
    product_list = []
    for product in similar_products:
        product_data = {
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
        selected_product = request.POST.get('selected_product')
        tender_id = request.POST.get('tender_id')
        selected_product_key = f'selected_product_{tender_id}'
        request.session[selected_product_key] = selected_product
        return redirect('similar_products', tender_id=tender_id)
    else:
        return JsonResponse({'error': 'Invalid request method.'})

