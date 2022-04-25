from rest_framework.response import Response
from rest_framework import viewsets

from .models import MortageOffer
from .serializers import MortageOfferSerializer

class OfferViewSet(viewsets.ViewSet):
    serializer_class = MortageOfferSerializer
    queryset = MortageOffer.objects.all()

