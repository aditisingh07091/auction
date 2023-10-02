from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuctionViewSet,BidView

router = DefaultRouter()
router.register(r'auctions', AuctionViewSet ,basename='auction')

urlpatterns = [
    path('', include(router.urls)),
    # path('', AuctionViewSet.as_view({'get': 'list', 'post': 'create'}), name='auction-list'),
    path('create/', AuctionViewSet.as_view({'post': 'create'}), name='create'),
    path('place_bid/<pk>/', BidView.as_view(), name='place_bid'),
    path('<int:pk>/', AuctionViewSet.as_view({ 'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='auction-detail'),
   
    
]
