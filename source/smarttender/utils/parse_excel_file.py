import math

import pandas as pd

from smarttender.models import RefTradeMethod, RefUnit, TrdBuy, Plan, Product, Supplier, Lot, Calculation


def parse_excel_file(excel_file):
    df = pd.read_excel(excel_file)
    empty_row_count = 0

    for index, row in df.iterrows():
        if pd.isnull(row[1]) and pd.isnull(row[2]) and pd.isnull(row[3]):
            empty_row_count += 1
        else:
            empty_row_count = 0

        if empty_row_count >= 2:
            break

        row = [value if not (isinstance(value, float) and math.isnan(value)) else None for value in row]

        # date = parse_date(row[18])
        # deadline = parse_date(row[19])

        # price_per_unit = parse_float(row[5])
        # count = parse_float(row[6])
        # planned_amount = parse_float(row[8])
        # purchase_price = parse_float(row[16])
        # profit_rate = parse_float(row[23])
        # delivery_rate = parse_float(row[24])
        # purchase_price_per_unit = parse_float(row[25])
        # budget_price_per_unit = parse_float(row[27])
        # overall_profit = parse_float(row[28])
        # overall_purchase_amount = parse_float(row[29])
        # overall_contract_amount = parse_float(row[30])
        # winning_price = parse_float(row[31])

        trade_method, _ = RefTradeMethod.objects.get_or_create(
            name_ru=row[20]
        )
        unit_measure, _ = RefUnit.objects.get_or_create(
            name_ru=row[7]
        )
        trd_buy = TrdBuy.objects.create(
            publish_date=row[18],
            end_date=row[19],
            ref_trade_methods=trade_method
        )
        plan = Plan.objects.create(
            price=row[5],
            count=row[6],
            ref_units=unit_measure,
            amount=row[8],
            supply_date_ru=row[9]
        )
        product, _ = Product.objects.get_or_create(
            trade_name=row[10]
        )
        supplier, _ = Supplier.objects.get_or_create(
            name=row[11]
        )
        lot = Lot.objects.create(
            lot_number=row[1],
            customer_name_ru=row[2],
            name_ru=row[3],
            description_ru=row[4]
        )
        lot.plans.set([plan])
        lot.trd_buy = trd_buy
        lot.save()
        lot.products.add(product)
        lot.suppliers.add(supplier)

        calculation = Calculation.objects.create(
            trd_buy=trd_buy,
            supplier_discount=row[12],
            vat=row[13],
            note=row[14],
            manager=row[15],
            purchase_price=row[16],
            overall_info=row[17],
            paper_ad_link=row[21],
            lot_link=row[22],
            profit_rate=row[23],
            delivery_rate=row[24],
            purchase_price_per_unit=row[25],
            bidding_price_per_unit=row[26],
            budget_price_per_unit=row[27],
            overall_profit=row[28],
            overall_purchase_amount=row[29],
            overall_contract_amount=row[30],
            winning_price=row[31],
            commercial_offer_text=row[32]
        )

# def parse_float(value):
#     if value and value != 'None':
#         value = str(value).replace(' ', '').replace(',', '.')
#         return float(value)
#     return None

# def parse_date(date_str):
#     try:
#         date = datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')
#     except ValueError:
#         try:
#             date = datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
#         except ValueError:
#             try:
#                 date = datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
#             except ValueError:
#                 raise ValueError("Invalid date format")
#     return date

# def parse_date(date_str):
#     try:
#         date = datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')
#     except ValueError:
#         date = datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
#     return date


# def parse_date(date_str):
#     try:
#         date = datetime.strptime(date_str, '%d.%m.%Y %H:%M:%S').strftime('%Y-%m-%d')
#     except ValueError:
#         try:
#             datetime_obj = datetime.strptime(date_str, '%d.%m.%Y')
#             if datetime_obj.time() == time(0, 0):
#                 date = datetime_obj.strftime('%Y-%m-%d')
#             else:
#                 date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
#         except ValueError:
#             try:
#                 datetime_obj = datetime.strptime(date_str, '%d/%m/%Y')
#                 if datetime_obj.time() == time(0, 0):
#                     date = datetime_obj.strftime('%Y-%m-%d')
#                 else:
#                     date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
#             except ValueError:
#                 try:
#                     datetime_obj = datetime.strptime(date_str, '%d-%m-%Y %H:%M:%S')
#                     if datetime_obj.time() == time(0, 0):
#                         date = datetime_obj.strftime('%Y-%m-%d')
#                     else:
#                         date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
#                 except ValueError:
#                     raise ValueError("Invalid date format")
#     return date
