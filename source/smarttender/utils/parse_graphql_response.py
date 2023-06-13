def parse_graphql_response(filtered_lots):
    for lot in filtered_lots:
        try:
            plans = lot.get('Plans', [])
            if plans:
                for plan in plans:
                    try:
                        plan['price'] = plan.get('price', None)
                        plan['count'] = plan.get('count', None)
                        ref_units = plan.get('RefUnits')
                        if ref_units and isinstance(ref_units, list):
                            for unit in ref_units:
                                unit['nameRu'] = unit.get('nameRu', None)
                        plan['amount'] = plan.get('amount', None)
                        plan['supplyDateRu'] = plan.get('supplyDateRu', None)
                        plan['refEnstruCode'] = plan.get('refEnstruCode', None)
                    except KeyError as e:
                        pass

            trd_buy = lot.get('TrdBuy')
            if trd_buy:
                try:
                    trd_buy['publishDate'] = trd_buy.get('publishDate', None)
                    trd_buy['endDate'] = trd_buy.get('endDate', None)
                    ref_trade_methods = trd_buy.get('RefTradeMethods')
                    if ref_trade_methods and isinstance(ref_trade_methods, list):
                        for trade_method in ref_trade_methods:
                            trade_method['nameRu'] = trade_method.get('nameRu', None)
                except KeyError as e:
                    pass

            files = lot.get('Files', [])
            if files:
                for file in files:
                    try:
                        file['filePath'] = file.get('filePath', None)
                    except KeyError as e:
                        pass
        except KeyError as e:
            pass

    return filtered_lots
