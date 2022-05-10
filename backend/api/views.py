from django.db.models import F, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import MortageOffer
from .serializers import MortageOfferSerializer, MortageOfferCreateSerializer
from .filters import OfferFilter
from services import get_monthly_payment


class OfferViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OfferFilter
    ordering_fields = ['rate_min',]


    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return MortageOfferCreateSerializer
        else:
            return MortageOfferSerializer


    def get_queryset(self):
        price = self.request.query_params.get('price')
        deposit = self.request.query_params.get('deposit')
        term = self.request.query_params.get('term')
        order = self.request.query_params.get('order')

        if not all([price, deposit, term]):
            queryset = MortageOffer.objects.all()
            return queryset
        amount = int(price) - int(deposit)
        queryset = MortageOffer.objects.filter(
            Q(payment_max__gte=amount) & (Q(payment_min__lte=amount)) & (Q(term_max__gte=term)) & (Q(term_min__lte=term)))\
            .annotate(payment=get_monthly_payment(amount=amount, loan_rate=F("rate_min"), years=int(term)))
        print(order)
        if order == "payment" or order == "-payment":
            queryset = queryset.order_by(order)
        return queryset

