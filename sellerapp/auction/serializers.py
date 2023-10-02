from rest_framework import serializers
from .models import Auction
from user.models import CustomUser

class AuctionSerializer(serializers.ModelSerializer):
    # winner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    class Meta:
        model = Auction
        
        fields = ['start_time', 'end_time', 'start_price', 'item_name', 'auction_id','highest_bid']
        
        # fields = '__all__'
