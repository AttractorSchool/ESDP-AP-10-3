import os
import tabula
from django.conf import settings
from django.shortcuts import render
from smarttender.models import Price, OptPrice


def pdf_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['pdf_file']
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(file_path, 'wb') as file:
            for chunk in uploaded_file.chunks():
                file.write(chunk)
        tables = tabula.read_pdf(file_path, pages='5-156', multiple_tables=False, encoding='cp1251')
        data = tables[0].values.tolist()
        header = data[0]
        rows = data[1:]
        for row in rows:
            trade_name = row[1].replace('-', '')
            mnn = row[2].replace('-', '')
            medicine = row[3].replace('-', '')
            registration_number = row[5]
            unit = row[6].replace('-', '')
            limit_price = row[7].replace('-', '')

            price = Price(
                trade_name=trade_name,
                mnn=mnn,
                medicine=medicine,
                registration_number=registration_number,
                unit=unit,
                limit_price=limit_price
            )
            price.save()

        os.remove(file_path)

    prices = Price.objects.all()
    return render(request, 'price_pdf.html', {'prices': prices})


def opt_pdf_price(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['pdf_file']
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(file_path, 'wb') as file:
            for chunk in uploaded_file.chunks():
                file.write(chunk)
        tables = tabula.read_pdf(file_path, pages='4-170',  multiple_tables=False, encoding='cp1251')
        data = tables[0].values.tolist()
        header = data[0]
        rows = data[1:]
        for row in rows:
            trade_name = row[1]
            mnn = row[2]
            medicine = row[3]
            registration_number = row[5]
            limit_price_producer = row[6]
            limit_price_opt = row[7]
            limit_price_per = row[8]

            price = OptPrice(
                trade_name=trade_name,
                mnn=mnn,
                medicine=medicine,
                registration_number=registration_number,
                limit_price_producer=limit_price_producer,
                limit_price_opt=limit_price_opt,
                limit_price_per=limit_price_per
            )
            price.save()

        os.remove(file_path)

    prices = OptPrice.objects.all()
    return render(request, 'opt_price_pdf.html', {'prices': prices})
