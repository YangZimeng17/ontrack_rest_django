from django.shortcuts import render
from django.http import JsonResponse
from .models import MaterialType

def import_material_type(request):
    existing_rows = []
    for row in MaterialType.objects.all():
        existing_rows.append(row.label)

    new_rows = []
    for row in MaterialType.getOriginalRows():
        if row['material_type'] not in existing_rows:
            new_rows.append(
                MaterialType(
                    label=row['material_type'],
                    description=row['description'],
                    active=row['active'],
                )
            )

    if new_rows:
        MaterialType.objects.bulk_create(new_rows)
        return JsonResponse({'message': str(len(new_rows)) + ' new material types are successfully added into database'}, status=201)

    return JsonResponse({'message': 'No material type is added into database'}, status=201)
