import math
from datetime import datetime

import pandas as pd
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView

from smarttender.models import Tender


class TenderListView(ListView):
    model = Tender
    template_name = 'index.html'
    context_object_name = 'tenders'
    ordering = 'created_at'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.FILES and 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                row = [value if not (isinstance(value, float) and math.isnan(value)) else None for value in row]
                date = datetime.strptime(row[17], '%d.%m.%Y').strftime('%Y-%m-%d')
                deadline = datetime.strptime(row[18], '%d.%m.%Y').strftime('%Y-%m-%d')
                price_per_unit = float(str(row[4]).replace(' ', '').replace(',', '.')) if row[4] and row[
                    4] != 'None' else None
                planned_amount = float(str(row[7]).replace(' ', '').replace(',', '.')) if row[7] and row[
                    7] != 'None' else None
                purchase_price = float(str(row[15]).replace(' ', '').replace(',', '.')) if row[15] and row[
                    15] != 'None' else None
                profit_rate = float(str(row[22]).replace(' ', '').replace(',', '.')) if row[22] and row[
                    22] != 'None' else None
                purchase_price_per_unit = float(str(row[24]).replace(' ', '').replace(',', '.')) if row[24] and row[
                    24] != 'None' else None
                budget_price_per_unit = float(str(row[26]).replace(' ', '').replace(',', '.')) if row[26] and row[
                    26] != 'None' else None
                overall_profit = float(str(row[27]).replace(' ', '').replace(',', '.')) if row[27] and row[
                    27] != 'None' else None
                overall_purchase_amount = float(str(row[28]).replace(' ', '').replace(',', '.')) if row[28] and row[
                    28] != 'None' else None
                overall_contract_amount = float(str(row[29]).replace(' ', '').replace(',', '.')) if row[29] and row[
                    29] != 'None' else None
                winning_price = float(str(row[30]).replace(' ', '').replace(',', '.')) if row[30] and row[
                    30] != 'None' else None
                tender = Tender(
                    lot=row[0],
                    company=row[1],
                    name=row[2],
                    additional_info=row[3],
                    price_per_unit=price_per_unit,
                    quantity=row[5],
                    measure_unit=row[6],
                    planned_amount=planned_amount,
                    delivery_deadline=row[8],
                    proposed_product_name=row[9],
                    supplier=row[10],
                    supplier_discount=row[11],
                    vat=row[12],
                    note=row[13],
                    manager=row[14],
                    purchase_price=purchase_price,
                    overall_info=row[16],
                    date=date,
                    deadline=deadline,
                    procurement_type=row[19],
                    paper_ad_link=row[20],
                    lot_link=row[21],
                    profit_rate=profit_rate,
                    delivery_rate=row[23],
                    purchase_price_per_unit=purchase_price_per_unit,
                    bidding_price_per_unit=row[25],
                    budget_price_per_unit=budget_price_per_unit,
                    overall_profit=overall_profit,
                    overall_purchase_amount=overall_purchase_amount,
                    overall_contract_amount=overall_contract_amount,
                    winning_price=winning_price,
                    commercial_offer_text=row[21],
                )
                tender.save()
            messages.success(request, 'Файл успешно загружен!')
        else:
            messages.error(request, 'Ошибка загрузки файла!')
        return redirect('index')