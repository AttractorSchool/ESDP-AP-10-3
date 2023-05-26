import math
from datetime import datetime

import pandas as pd
from django.contrib import messages
from django.views.generic import ListView
from smarttender.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def post(self, request, *args, **kwargs):
        if request.FILES and 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                row = [value if not (isinstance(value, float) and math.isnan(value)) else None for value in row]
                a = row[5].replace(' ', '').replace(',', '.')
                register_date = datetime.strptime(str(a), '%d.%m.%Y').strftime('%Y-%m-%d') if row[5] is not None else None
                #time = datetime.strptime(str(row[6]), '%d.%m.%Y').strftime('%Y-%m-%d') if row[6] is not None else None
                deadline = datetime.strptime(str(row[7]), '%d.%m.%Y').strftime('%Y-%m-%d') if row[7] is not None else None
                product = Product(
                    number=row[0],
                    register_number=row[1],
                    type=row[2],
                    trade_name=row[3],
                    view=row[4],
                    register_date=register_date,
                    time=row[6],
                    deadline=deadline,
                    producer=row[8],
                    country=row[9],
                    classification=row[10],
                    IGN=row[11],
                    atx_classification=row[12],
                    med_form=row[13],
                    release_form=row[14],
                    shelf_life=row[15],
                    GMP=row[16],
                    generic=row[17],
                    recipe=row[18],
                    trademark=row[19],
                    patent=row[20],
                    nd_type=row[21],
                    nd_number=row[22],
                    dosage_and_concentration=row[23],
                )
                product.save()
            messages.success(request, 'Файл успешно загружен!')
        else:
            messages.error(request, 'Ошибка загрузки файла!')
        return self.get(request, *args, **kwargs)
