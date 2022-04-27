from rest_framework.response import Response
from rest_framework import viewsets
from .models import MortageOffer
from .serializers import MortageOfferSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = MortageOfferSerializer
    queryset = MortageOffer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['term_min', ]

