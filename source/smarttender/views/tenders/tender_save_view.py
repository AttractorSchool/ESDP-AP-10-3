import json
import asyncio
import httpx
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.settings import GRAPHQL_URL
from smarttender.models import RefTradeMethod, RefUnit, TrdBuy, Plan, Lot


async def execute_graphql_query(query, variables):
    async with httpx.AsyncClient() as client:
        response = await client.post(GRAPHQL_URL, json={'query': query, 'variables': variables})
        response.raise_for_status()
        return response.json()


@csrf_exempt
def tender_save_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_tenders = data.get('selectedTenders', [])
            tasks = []

            for tender in selected_tenders:
                if not Lot.objects.filter(
                        lot_number=tender.get('lotNumber'),
                        customer_name_ru=tender.get('customerNameRu'),
                        name_ru=tender.get('nameRu')
                ).exists():
                    trade_method = RefTradeMethod.objects.create(
                        name_ru=tender.get('refTradeMethod')
                    )
                    unit_measure = RefUnit.objects.create(
                        name_ru=tender.get('refUnit')
                    )
                    trd_buy = TrdBuy.objects.create(
                        publish_date=tender.get('publishDate'),
                        end_date=tender.get('endDate'),
                        ref_trade_methods=trade_method
                    )
                    plan = Plan.objects.create(
                        price=tender.get('price'),
                        count=tender.get('count'),
                        ref_units=unit_measure,
                        amount=tender.get('amount'),
                        supply_date_ru=tender.get('supplyDateRu')
                    )
                    lot = Lot.objects.create(
                        lot_number=tender.get('lotNumber'),
                        customer_name_ru=tender.get('customerNameRu'),
                        name_ru=tender.get('nameRu'),
                        description_ru=tender.get('descriptionRu'),
                        plans=plan,
                        trd_buy=trd_buy
                    )
                    tender = TrdBuy.objects.create(
                        lot=lot
                    )

                    query = '''
                        query($filter: LotsFiltersInput){
                            Lots(filter: $filter) {
                                trdBuyNumberAnno
                            }
                        }
                        '''
                    variables = {
                        'filter': {
                            'lotNumber': tender.get('lotNumber')
                        }
                    }

                    task = asyncio.ensure_future(execute_graphql_query(query, variables))
                    tasks.append(task)

                    # Wait for all async tasks to complete
                    results = asyncio.gather(*tasks)

                    # Process the results
                    for result in results:
                        trd_buy_number = result['data']['Lots'][0]['trdBuyNumberAnno']
                        # Update the TrdBuy model for the Lot using the obtained trd_buy_number

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
