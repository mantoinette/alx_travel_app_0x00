from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """Serializer for Listing model."""
    class Meta:
        model = Listing
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model."""
    class Meta:
        model = Booking
        fields = '__all__'
