from rest_framework import generics
from .serializers import SnackSerializer
from snacks.models import Snack


class SnacksListAPIView(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnacksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
