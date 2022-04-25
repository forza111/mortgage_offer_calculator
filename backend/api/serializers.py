from rest_framework import serializers
from .models import MortageOffer

class MortageOfferSerializer(serializers.Serializer):
    class Meta:
        model = MortageOffer
        exclude = ("id", )
