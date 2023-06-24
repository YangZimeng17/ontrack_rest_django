from django.db import models
from django.db import connections

class MaterialType(models.Model):
    label = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250, default='')
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
    @classmethod
    def getOriginalRows(cls):
        with connections['original'].cursor() as cursor:
            cursor.execute('''
                SELECT material_type.*, language.EN as description
                FROM material_type
                LEFT JOIN language ON language.label=material_type.material_type
            ''')
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]