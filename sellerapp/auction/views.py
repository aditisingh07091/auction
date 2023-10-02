from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Auction
from .serializers import AuctionSerializer
from user.authentication import StaticAPIAuthentication
from django.utils import timezone
from user.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class IsAdminUserOrReadOnly(permissions.BasePermission):
  

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        
        return request.user and request.user.is_staff

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    authentication_classes = [StaticAPIAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]
    
    def post(self, request):
        serializer = AuctionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
   


class BidView(APIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    
    @action(detail=True, methods=['post'], url_path='place_bid', permission_classes=[IsAuthenticated],authentication_classes=[])
    def place_bid(self, request, pk=None):
        auction = self.get_object()

        
        current_time = timezone.now()
        if current_time < auction.start_time or current_time > auction.end_time:
            return Response({"error": "Auction is not active."}, status=400)

        bid_amount = request.data.get('bid_amount')
        if bid_amount is None:
            return Response({"error": "Bid amount is required."}, status=400)

        if bid_amount <= auction.highest_bid:
            return Response({"error": "Bid amount should be greater than the start price."}, status=400)

        auction.highest_bid = bid_amount
        auction.user = request.user
        auction.save()


        return Response({"message": "Bid placed successfully."}, status=200)
    
 

    

    
    