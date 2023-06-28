# def parse_graphql_response(filtered_lots):
#     for lot in filtered_lots:
#         try:
#             plans = lot.get('Plans', [])
#             if plans:
#                 for plan in plans:
#                     try:
#                         plan['price'] = plan.get('price', None)
#                         plan['count'] = plan.get('count', None)
#                         ref_units = plan.get('RefUnits')
#                         if ref_units and isinstance(ref_units, list):
#                             for unit in ref_units:
#                                 unit['nameRu'] = unit.get('nameRu', None)
#                         plan['amount'] = plan.get('amount', None)
#                         plan['supplyDateRu'] = plan.get('supplyDateRu', None)
#                         plan['refEnstruCode'] = plan.get('refEnstruCode', None)
#                     except KeyError as e:
#                         pass
#
#             trd_buy = lot.get('TrdBuy')
#             if trd_buy:
#                 try:
#                     trd_buy['publishDate'] = trd_buy.get('publishDate', None)
#                     trd_buy['endDate'] = trd_buy.get('endDate', None)
#                     ref_trade_methods = trd_buy.get('RefTradeMethods')
#                     if ref_trade_methods and isinstance(ref_trade_methods, list):
#                         for trade_method in ref_trade_methods:
#                             trade_method['nameRu'] = trade_method.get('nameRu', None)
#                 except KeyError as e:
#                     pass
#
#             files = lot.get('Files', [])
#             if files:
#                 for file in files:
#                     try:
#                         file['filePath'] = file.get('filePath', None)
#                     except KeyError as e:
#                         pass
#         except KeyError as e:
#             pass
#
#     return filtered_lots

def parse_graphql_response(filtered_trd_buys):
    for trd_buy in filtered_trd_buys:
        try:
            trd_buy['numberAnno'] = trd_buy.get('numberAnno', None)
            trd_buy['publishDate'] = trd_buy.get('publishDate', None)
            trd_buy['endDate'] = trd_buy.get('endDate', None)
            trd_buy['customerNameRu'] = trd_buy.get('customerNameRu', None)
            trd_buy['nameRu'] = trd_buy.get('nameRu', None)
            ref_trade_methods = trd_buy.get('RefTradeMethods', [])
            for i in range(len(ref_trade_methods)):
                ref_trade_methods[i] = ref_trade_methods[i].get('nameRu', None)

            lots = trd_buy.get('Lots', [])
            for lot in lots:
                try:
                    lot['lotNumber'] = lot.get('lotNumber', None)
                    lot['refLotStatusId'] = lot.get('refLotStatusId', None)
                    lot['lastUpdateDate'] = lot.get('lastUpdateDate', None)
                    lot['count'] = lot.get('count', None)
                    lot['amount'] = lot.get('amount', None)
                    lot['nameKz'] = lot.get('nameKz', None)
                    lot['nameRu'] = lot.get('nameRu', None)
                    lot['descriptionKz'] = lot.get('descriptionKz', None)
                    lot['descriptionRu'] = lot.get('descriptionRu', None)
                    lot['customerNameKz'] = lot.get('customerNameKz', None)
                    lot['customerNameRu'] = lot.get('customerNameRu', None)
                    lot['trdBuyNumberAnno'] = lot.get('trdBuyNumberAnno', None)
                    lot['dumping'] = lot.get('dumping', None)
                    lot['pointList'] = lot.get('pointList', None)

                    plans = lot.get('Plans', [])
                    for plan in plans:
                        try:
                            plan['id'] = plan.get('id', None)
                            plan['subjectNameKz'] = plan.get('subjectNameKz', None)
                            plan['subjectNameRu'] = plan.get('subjectNameRu', None)
                            plan['nameKz'] = plan.get('nameKz', None)
                            plan['nameRu'] = plan.get('nameRu', None)
                            plan['refUnitsCode'] = plan.get('refUnitsCode', None)
                            plan['count'] = plan.get('count', None)
                            plan['price'] = plan.get('price', None)
                            plan['amount'] = plan.get('amount', None)
                            plan['refEnstruCode'] = plan.get('refEnstruCode', None)
                            plan['dateCreate'] = plan.get('dateCreate', None)
                            plan['descKz'] = plan.get('descKz', None)
                            plan['descRu'] = plan.get('descRu', None)
                            plan['supplyDateRu'] = plan.get('supplyDateRu', None)

                            ref_units = plan.get('RefUnits', [])
                            for unit in ref_units:
                                unit['nameKz'] = unit.get('nameKz', None)
                                unit['nameRu'] = unit.get('nameRu', None)
                        except KeyError:
                            pass

                    files = lot.get('Files', [])
                    for file in files:
                        try:
                            file['originalName'] = file.get('originalName', None)
                            file['nameKz'] = file.get('nameKz', None)
                            file['nameRu'] = file.get('nameRu', None)
                            file['filePath'] = file.get('filePath', None)
                        except KeyError:
                            pass
                except KeyError:
                    pass
        except KeyError:
            pass

    return filtered_trd_buys

