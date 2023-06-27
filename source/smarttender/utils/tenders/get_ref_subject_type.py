from smarttender.models import RefSubjectType


def get_ref_subject_type(subject_type):
    try:
        ref_subject_type, created = RefSubjectType.objects.get_or_create(
            name_kz=subject_type.get('nameKz'),
            name_ru=subject_type.get('nameRu')
        )
        return ref_subject_type
    except KeyError:
        pass
