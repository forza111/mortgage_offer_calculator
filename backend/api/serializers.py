from rest_framework import serializers
from .models import MortgageOffer


class MortgageOfferSerializer(serializers.ModelSerializer):
    payment = serializers.IntegerField(required=False)

    class Meta:
        model = MortgageOffer
        fields = "__all__"


class MortgageOfferCreateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def validate(self, data):
        if not 1 <= data["term_min"] <= 80:
            raise serializers.ValidationError({"term_min": "Допустимый диапазон значений: 1-80 "})
        if not 1 <= data["term_max"] <= 80:
            raise serializers.ValidationError({"term_max": "Допустимый диапазон значений: 1-80 "})
        if not 1 <= data["rate_min"] <= 45:
            raise serializers.ValidationError({"rate_min": "Допустимый диапазон значений: 1-45 "})
        if not 1 <= data["rate_max"] <= 45:
            raise serializers.ValidationError({"rate_max": "Допустимый диапазон значений: 1-45 "})
        if not 10000 <= data["payment_min"] <= 1000000000:
            raise serializers.ValidationError({"payment_min": "Допустимый диапазон значений: 10000-1000000000 "})
        if not 10000 <= data["payment_max"] <= 1000000000:
            raise serializers.ValidationError({"payment_max": "Допустимый диапазон значений: 10000-1000000000 "})
        if data["term_min"] >= data["term_max"]:
            raise serializers.ValidationError({"term_max": "Значение должно быть больше term_min"})
        if data["rate_min"] >= data["rate_max"]:
            raise serializers.ValidationError({"rate_max": "Значение должно быть больше rate_min"})
        if data["payment_min"] >= data["payment_max"]:
            raise serializers.ValidationError({"payment_max": "Значение должно быть больше payment_min"})
        return data

    class Meta:
        model = MortgageOffer
        fields = "__all__"
