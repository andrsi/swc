from rest_framework import routers

from api import views

app_name = 'api'

router = routers.SimpleRouter()
router.register('shortlink', views.ShortLinkViewSet, basename='shortlink')

urlpatterns = router.urls + [
]
