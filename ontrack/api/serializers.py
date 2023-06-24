from rest_framework import serializers
from materialmanager.models import MaterialType

class MaterialTypeSerializer(serializers.ModelSerializer):
    createdAt = serializers.ReadOnlyField()
    updatedAt = serializers.ReadOnlyField()

    class Meta:
        model = MaterialType
        fields = ['id', 'label', 'description', 'active', 'createdAt', 'updatedAt']