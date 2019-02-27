from rest_framework import serializers
from .models import Track


class TrackSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'url', 'amount')
