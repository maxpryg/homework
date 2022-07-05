from rest_framework import serializers
from firstapp.models import Store


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'rating']
