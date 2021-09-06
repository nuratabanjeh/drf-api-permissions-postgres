from rest_framework import serializers
from .models import Snacks

class SnacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snacks
        fields = ('id','snack_name','description','author')