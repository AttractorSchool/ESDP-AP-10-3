import math

import pandas as pd
import requests
import urllib3

from app.settings import AUTH_TOKEN, GRAPHQL_URL
from smarttender.models import RefTradeMethod, RefUnit, TrdBuy, Plan, Product, Supplier, Lot, Calculation, Offer


def parse_excel_file(excel_file):
    df = pd.read_excel(excel_file)

    for index, row in df.iterrows():
        is_empty = pd.isnull(row[1]) and pd.isnull(row[2]) and pd.isnull(row[3])
        if is_empty:
            continue
        else:
            empty_row_count = 0

        if empty_row_count >= 2:
            break

        row = [value if not (isinstance(value, float) and math.isnan(value)) else None for value in row]
        lot_number = row[1]
        trd_buy_number_anno = None

        if lot_number is not None and isinstance(lot_number, str) and len(lot_number) >= 8:
            query = '''
                    {
                        Lots(filter: {lotNumber: "%s"})
                        {
                            trdBuyNumberAnno
                        }
                    }
                    ''' % lot_number

            headers = {
                'Authorization': f'Bearer {AUTH_TOKEN}',
                'Content-Type': 'application/json'
            }
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.post(GRAPHQL_URL, json={'query': query}, headers=headers, verify=False)
            response_data = response.json()
            lots = response_data['data']['Lots']
            if lots:
                trd_buy_number_anno = lots[0]['trdBuyNumberAnno']

        if not Lot.objects.filter(
                lot_number=row[1],
                customer_name_ru=row[2],
                name_ru=row[3]
        ).exists():
            trade_method, _ = RefTradeMethod.objects.get_or_create(
                name_ru=row[20]
            )
            unit_measure, _ = RefUnit.objects.get_or_create(
                name_ru=row[7]
            )
            trd_buy = TrdBuy.objects.create(
                publish_date=row[18],
                end_date=row[19],
                ref_trade_methods=trade_method,
                number_anno=trd_buy_number_anno
            )
            plan = Plan.objects.create(
                price=row[5],
                count=row[6],
                amount=row[8],
                supply_date_ru=row[9]
            )
            plan.ref_units.set([unit_measure])

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
            offer = Offer.objects.create(
                product=product,
                supplier=supplier,
                lot=lot
            )
            calculation = Calculation.objects.create(
                lot=lot,
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
