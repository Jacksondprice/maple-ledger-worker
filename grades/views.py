from rest_framework import viewsets

from .models import Grade
from .serializers import GradeSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.order_by("id")
    serializer_class = GradeSerializer
