from smarttender.models import File


def create_file(lot, file):
    try:
        file = File(
            original_name=file.get('originalName'),
            name_kz=file.get('nameKz'),
            name_ru=file.get('nameRu'),
            file_path=file.get('filePath'),
            lot=lot
        )
        file.save()
    except KeyError:
        pass
    return file
