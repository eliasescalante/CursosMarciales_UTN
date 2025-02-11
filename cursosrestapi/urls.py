from rest_framework import routers
from .viewset import CursosRestApiViewSet

router=routers.SimpleRouter()
router.register('cursosrestapi', CursosRestApiViewSet)
urlpatterns=router.urls
