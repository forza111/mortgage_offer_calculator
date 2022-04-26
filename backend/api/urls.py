from django.urls import path

from .views import OfferViewSet

urlpatterns = [
    path('offer/', OfferViewSet.as_view({"post": "create", "get": "list"})),
    path('offer/<int:pk>', OfferViewSet.as_view({"patch": "partial_update", "delete": "destroy"})),
]
