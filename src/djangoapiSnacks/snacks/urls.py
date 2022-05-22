from django.urls import path
from snacks.api.viewset import (
                                SnacksListAPIView,
                                SnacksDetailAPIView
                                )

urlpatterns = [
    path('api/v1/snacks-list', SnacksListAPIView.as_view(), name='snacks_list'),
    path('api/v1/<int:pk>', SnacksDetailAPIView.as_view(), name='snacks_detail'),

]