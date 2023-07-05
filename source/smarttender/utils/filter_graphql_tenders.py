from smarttender.models import EnsTruCode


def filter_graphql_tenders(tenders, search_value):
    filtered_tenders = []

    if search_value:
        for tender in tenders:
            for lot in tender['Lots'] if tender['Lots'] else None:
                for plan in lot['Plans'] if lot['Plans'] else None:
                    if 'refEnstruCode' in plan and search_value in plan['refEnstruCode']:
                        filtered_tenders.append(tender)
                        break
    else:
        filtered_tenders = tenders
        # for tender in tenders:
        #     filtered_tenders.append(tender)
        #     break
        # for plan in lot['Plans']:
        #     if 'refEnstruCode' in plan:
        #         ref_enstru_code = plan['refEnstruCode']
        #         matching_codes = [ens_tru_code for ens_tru_code in EnsTruCode.objects.all() if
        #                           ref_enstru_code in ens_tru_code.code]
        #         if matching_codes:
        #             filtered_tenders.append(tender)
        #             break

    return filtered_tenders
