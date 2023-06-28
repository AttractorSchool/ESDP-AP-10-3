from smarttender.models import RefUnit


def get_ref_units(ref_unit):
    try:
        ref_unit, created = RefUnit.objects.get_or_create(
            name_kz=ref_unit.get('nameKz'),
            name_ru=ref_unit.get('nameRu')
        )
    except KeyError:
        pass
    return ref_unit
