from smarttender.models import EnsTruCode


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
        for lot in lots:
            plans = lot.get('Plans', [])
            for plan in plans:
                if 'refEnstruCode' in plan:
                    ref_enstru_code = plan['refEnstruCode']
                    matching_codes = [ens_tru_code for ens_tru_code in EnsTruCode.objects.all() if
                                      ref_enstru_code in ens_tru_code.code]
                    if matching_codes:
                        filtered_lots.append(lot)
                        break

    return filtered_lots
