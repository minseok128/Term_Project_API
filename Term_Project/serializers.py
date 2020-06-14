from rest_framework import serializers
from .models import Extinguisher


class ExtinguisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extinguisher
        fields = ('num', 'location', 'local_num', 'last_check', 'fire_state')
