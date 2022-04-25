# from django.urls import path
#
# from .views import OfferViewSet
#
# app_name = "api"
#
# urlpatterns = [
#     path('offer/', OfferViewSet.as_view({"get": "list"}))
# ]


from rest_framework.routers import DefaultRouter

from .views import OfferViewSet

router = DefaultRouter()
router.register(r"offer", OfferViewSet, basename='user')

urlpatterns = router.urls
