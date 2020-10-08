from rest_framework import serializers

from .models import Nickname

class NicknameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nickname
        fields = ('id','name', 'petname')