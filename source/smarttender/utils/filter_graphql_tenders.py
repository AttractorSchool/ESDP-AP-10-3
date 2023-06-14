def filter_graphql_tenders(lots, search_value):
    filtered_lots = []

    if search_value:
        for lot in lots:
            plans = lot.get('Plans', [])
            for plan in plans:
                if 'refEnstruCode' in plan and search_value in plan['refEnstruCode']:
                    filtered_lots.append(lot)
                    break
    else:
        filtered_lots = lots

    return filtered_lots
