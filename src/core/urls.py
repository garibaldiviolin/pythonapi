from rest_framework import routers

from .views import EmployeeViewSet

router = routers.SimpleRouter()
router.register(r'employees', EmployeeViewSet)
urlpatterns = router.urls
