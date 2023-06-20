import asyncio
import json
from asgiref.sync import async_to_sync

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from graphqlclient import GraphQLClient

from app.settings import GRAPHQL_URL
from smarttender.models import TrdBuy, Lot


def execute_graphql_query(lot_number):
    client = GraphQLClient(GRAPHQL_URL)  # Replace with your GraphQL endpoint URL

    query = '''
    query Lots($lotNumber: String!) {
        Lots(filter: {lotNumber: $lotNumber}) {
            trdBuyNumberAnno
        }
    }
    '''

    variables = {
        'lotNumber': lot_number
    }

    result = client.execute(query, variables)
    return result


@csrf_exempt
def tender_save_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_tenders = data.get('selectedTenders', [])

            async def process_tender(tender):
                lot_number = tender.get('lotNumber')
                # Asynchronously execute the GraphQL query
                result = await execute_graphql_query(lot_number)

                # Parse the GraphQL response
                response = json.loads(result)
                trd_buy_number_anno = response['data']['Lots'][0]['trdBuyNumberAnno']

                # Retrieve or create the corresponding Lot object
                lot, created = Lot.objects.get_or_create(
                    lot_number=lot_number,
                    customer_name_ru=tender.get('customerNameRu'),
                    name_ru=tender.get('nameRu')
                )

                # Create or update the TrdBuy object for the Lot
                trd_buy, created = TrdBuy.objects.update_or_create(
                    lot=lot,
                    defaults={
                        'trd_buy_number_anno': trd_buy_number_anno
                    }
                )

            # Synchronously process the selected tenders
            coroutines = [process_tender(tender) for tender in selected_tenders]
            async_to_sync(asyncio.gather)(*coroutines)

            # for tender in selected_tenders:
            #     if not Lot.objects.filter(
            #             lot_number=tender.get('lotNumber'),
            #             customer_name_ru=tender.get('customerNameRu'),
            #             name_ru=tender.get('nameRu')
            #     ).exists():
            #         trade_method = RefTradeMethod.objects.create(
            #             name_ru=tender.get('refTradeMethod')
            #         )
            #         unit_measure = RefUnit.objects.create(
            #             name_ru=tender.get('refUnit')
            #         )
            #         trd_buy = TrdBuy.objects.create(
            #             publish_date=tender.get('publishDate'),
            #             end_date=tender.get('endDate'),
            #             ref_trade_methods=trade_method
            #         )
            #         plan = Plan.objects.create(
            #             price=tender.get('price'),
            #             count=tender.get('count'),
            #             ref_units=unit_measure,
            #             amount=tender.get('amount'),
            #             supply_date_ru=tender.get('supplyDateRu')
            #         )
            #         lot = Lot.objects.create(
            #             lot_number=tender.get('lotNumber'),
            #             customer_name_ru=tender.get('customerNameRu'),
            #             name_ru=tender.get('nameRu'),
            #             description_ru=tender.get('descriptionRu'),
            #             plans=plan,
            #             trd_buy=trd_buy
            #         )
            #         tender = TrdBuy.objects.create(
            #             lot=lot
            #         )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
