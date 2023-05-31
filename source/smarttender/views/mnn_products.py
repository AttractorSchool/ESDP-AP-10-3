from django.shortcuts import render

from smarttender.models import Tender, Product

def index(request):
    tenders = Tender.objects.all()
    mnn_products = Product.objects.filter(trade_name__contains=tenders.values('name'))
    context = {'mnn_products': mnn_products}
    return render(request, 'index.html', context)