import json
from datetime import date

import requests
import urllib3
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from smarttender.utils import send_graphql_request, filter_graphql_tenders, parse_graphql_response

# GRAPHQL_QUERY = '''
#     {
#         Lots(limit: 200) {
#             lotNumber
#             customerNameRu
#             nameRu
#             descriptionRu
#             Plans {
#                 price
#                 count
#                 RefUnits {
#                     nameRu
#                 }
#                 amount
#                 supplyDateRu
#                 refEnstruCode
#             }
#             TrdBuy {
#                 publishDate
#                 endDate
#                 RefTradeMethods {
#                     nameRu
#                 }
#             }
#             Files {
#                 filePath
#             }
#         }
#     }
#     '''

CURRENT_DATE = date.today().isoformat()
GRAPHQL_QUERY = '''
{
    TrdBuy(filter: {publishDate: "%s"})
    {
        id
        numberAnno
        nameKz
        nameRu
        totalSum
        countLots
        customerNameKz
        customerNameRu
        orgBin
        orgPid
        orgNameKz
        orgNameRu
        startDate
        repeatStartDate
        endDate
        publishDate
        itogiDatePublic
        discusStartDate
        discusEndDate
        lastUpdateDate
        finYear
        kato
        Files
        {
            originalName
            nameKz
            nameRu
            filePath
        }
        Lots
        {
            id
            lotNumber
            refLotStatusId
            lastUpdateDate
            count
            amount
            nameKz
            nameRu
            descriptionKz
            descriptionRu
            customerNameKz
            customerNameRu
            trdBuyNumberAnno
            dumping
            pointList
            Plans
            {
                id
                subjectNameKz
                subjectNameRu
                nameKz
                nameRu
                refUnitsCode
                count
                price
                amount
                refEnstruCode
                dateCreate
                descKz
                descRu
                supplyDateRu
                RefUnits
                {
                    nameKz
                    nameRu
                }
            }
            Files
            {
                originalName
                nameKz
                nameRu
                filePath
            }            
        }
        RefTradeMethods
            {
                id
                nameKz
                nameRu
                code
                symbolCode
            }
        RefSubjectType
        {
            id
            nameKz
            nameRu
        }
        RefBuyStatus
        {
            id
            nameKz
            nameRu
            code
        }
        RefTypeTrade
        {
            id
            nameKz
            nameRu
        }
    }
}
''' % CURRENT_DATE

@csrf_exempt
def tender_graphql_view(request: WSGIRequest):
    if request.method == 'POST':
        body_str = request.body.decode('utf-8')
        data = json.loads(body_str)
        search_value = data.get('search_value')

        data = send_graphql_request(GRAPHQL_QUERY)
        tenders = data.get('TrdBuy', [])
        filtered_tenders = filter_graphql_tenders(tenders, search_value)
        tenders = parse_graphql_response(filtered_tenders)

        return JsonResponse({'tenders': tenders})

# @csrf_exempt
# def tender_graphql_view(request: WSGIRequest):
#     if request.method == 'POST':
#         body_str = request.body.decode('utf-8')
#         data = json.loads(body_str)
#         search_value = data.get('search_value')
#         graphql_query = '''
#             {
#                 Lots {
#                     lotNumber
#                     customerNameRu
#                     nameRu
#                     descriptionRu
#                     Plans {
#                         price
#                         count
#                         RefUnits {
#                             nameRu
#                         }
#                         amount
#                         supplyDateRu
#                         refEnstruCode
#                     }
#                     TrdBuy {
#                         publishDate
#                         endDate
#                         RefTradeMethods {
#                             nameRu
#                         }
#                     }
#                     Files {
#                         filePath
#                     }
#                 }
#             }
#             '''
#         graphql_url = 'https://ows.goszakup.gov.kz/v3/graphql'
#         auth_token = '4c47e9fc44b56c35a1c7aa7f0dcb8b04'
#         headers = {
#             'Authorization': f'Bearer {auth_token}',
#             'Content-Type': 'application/json'
#         }
#         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#         response = requests.post(graphql_url, json={'query': graphql_query}, headers=headers, verify=False)
#         data = response.json().get('data')
#
#         lots = data.get('Lots', [])
#         filtered_lots = []
#
#         if search_value:
#             for lot in lots:
#                 plans = lot.get('Plans', [])
#                 for plan in plans:
#                     if 'refEnstruCode' in plan and search_value in plan['refEnstruCode']:
#                         filtered_lots.append(lot)
#                         break
#         else:
#             filtered_lots = lots
#
#         for lot in filtered_lots:
#             try:
#                 plans = lot.get('Plans', [])
#                 if plans:
#                     for plan in plans:
#                         try:
#                             plan['price'] = plan.get('price', None)
#                             plan['count'] = plan.get('count', None)
#                             ref_units = plan.get('RefUnits')
#                             if ref_units and isinstance(ref_units, list):
#                                 for unit in ref_units:
#                                     unit['nameRu'] = unit.get('nameRu', None)
#                             plan['amount'] = plan.get('amount', None)
#                             plan['supplyDateRu'] = plan.get('supplyDateRu', None)
#                             plan['refEnstruCode'] = plan.get('refEnstruCode', None)
#                         except KeyError as e:
#                             pass
#
#                 trd_buy = lot.get('TrdBuy')
#                 if trd_buy:
#                     try:
#                         trd_buy['publishDate'] = trd_buy.get('publishDate', None)
#                         trd_buy['endDate'] = trd_buy.get('endDate', None)
#                         ref_trade_methods = trd_buy.get('RefTradeMethods')
#                         if ref_trade_methods and isinstance(ref_trade_methods, list):
#                             for trade_method in ref_trade_methods:
#                                 trade_method['nameRu'] = trade_method.get('nameRu', None)
#                     except KeyError as e:
#                         pass
#
#                 files = lot.get('Files', [])
#                 if files:
#                     for file in files:
#                         try:
#                             file['filePath'] = file.get('filePath', None)
#                         except KeyError as e:
#                             pass
#             except KeyError as e:
#                 pass
#
#         return JsonResponse({'tenders': filtered_lots})

# for lot in filtered_lots:
#     plans = lot.get('Plans', [])
#     if plans:
#         for plan in plans:
#             if 'price' not in plan:
#                 plan['price'] = None
#             if 'count' not in plan:
#                 plan['count'] = None
#             ref_units = plan.get('RefUnits')
#             if ref_units:
#                 if ref_units and isinstance(ref_units, list):
#                     for unit in ref_units:
#                         if 'nameRu' not in unit:
#                             unit['nameRu'] = None
#             if 'amount' not in plan:
#                 plan['amount'] = None
#             if 'supplyDateRu' not in plan:
#                 plan['supplyDateRu'] = None
#             if 'refEnstruCode' not in plan:
#                 plan['refEnstruCode'] = None
#
#     trd_buy = lot.get('TrdBuy')
#     if trd_buy:
#         if 'publishDate' not in trd_buy:
#             trd_buy['publishDate'] = None
#         if 'endDate' not in trd_buy:
#             trd_buy['endDate'] = None
#         ref_trade_methods = trd_buy.get('RefTradeMethods')
#         if ref_trade_methods:
#             if ref_trade_methods and isinstance(ref_trade_methods, list):
#                 for trade_method in ref_trade_methods:
#                     if 'nameRu' not in trade_method:
#                         trade_method['nameRu'] = None
#
#     files = lot.get('Files', [])
#     if files:
#         for file in files:
#             if 'filePath' not in file:
#                 file['filePath'] = None
#
# return JsonResponse({'tenders': filtered_lots})

# import http.client
# import json
#
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
#
# @csrf_exempt
# def parse_tenders_view(request):
#     if request.method == 'POST':
#         graphql_query = '''
#             {
#                 Lots {
#                     lotNumber
#                     customerNameRu
#                     nameRu
#                     descriptionRu
#                     Plans {
#                         price
#                         count
#                         RefUnits {
#                             nameRu
#                         }
#                         amount
#                         supplyDateRu
#                         refEnstruCode
#                     }
#                     TrdBuy {
#                         publishDate
#                         endDate
#                         RefTradeMethods {
#                             nameRu
#                         }
#                     }
#                     Files {
#                         filePath
#                     }
#                 }
#             }
#             '''
#         auth_token = '4c47e9fc44b56c35a1c7aa7f0dcb8b04'
#         headers = {
#             'Authorization': f'Bearer {auth_token}',
#             'Content-Type': 'application/json'
#         }
#
#         connection = http.client.HTTPSConnection('ows.goszakup.gov.kz')
#         connection.request('POST', '/v3/graphql', body=graphql_query, headers=headers)
#         response = connection.getresponse()
#         response_data = response.read().decode()
#         connection.close()
#
#         data = json.loads(response_data).get('data')
#
#         return JsonResponse({'tenders': data.get('Lots', [])})
