from rest_framework.viewsets import ModelViewSet
from .models import Cars
from .serializer import CarsSerializer

class CarsViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
