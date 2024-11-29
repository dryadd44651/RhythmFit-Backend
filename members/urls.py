from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterView  # 確保這裡的引用正確
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'exercises', views.ExerciseViewSet, basename='exercise')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),  # 註冊 API 路徑
    # path('api/', include(router.urls)),
]
