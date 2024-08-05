from  rest_framework import serializers

from store.models import Item

class ItemSerialier(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
