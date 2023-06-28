from smarttender.models import Plan


def create_plan(lot, plan):
    try:
        plan = Plan(
            lot=lot,
            subject_name_kz=plan.get('subjectNameKz'),
            subject_name_ru=plan.get('subjectNameRu'),
            name_kz=plan.get('nameKz'),
            name_ru=plan.get('nameRu'),
            count=plan.get('count'),
            price=plan.get('price'),
            amount=plan.get('amount'),
            ref_enstru_code=plan.get('refEnstruCode'),
            desc_kz=plan.get('descKz'),
            desc_ru=plan.get('descRu'),
            supply_date_ru=plan.get('supplyDateRu')
        )
        plan.save()
    except KeyError:
        pass
    return plan
