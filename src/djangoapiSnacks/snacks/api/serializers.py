from pyexpat import model
from rest_framework import serializers
from snacks.models import Snack


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','description','title')
        model = Snack


# JSON