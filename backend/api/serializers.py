from rest_framework import serializers
from .models import MortageOffer

class MortageOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortageOffer
        exclude = ("id", )
        # fields = ("__all__")
