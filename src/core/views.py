from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    lookup_field = "name"
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
