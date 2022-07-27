from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

# step1: create a router
router = DefaultRouter()

# step2: register our viewset with default router to generate all urls
router.register('viewset', views.HelloViewSet, basename='viewset')
router.register('profile', views.UserProfileViewSet)    # not providing basename because DRF finds out name from the queryset which is present in UserProfileViewSet



urlpatterns = [
    path('apiview/', views.HelloApiView.as_view()),

    # step3: include those urls in our url pattern
    path('', include(router.urls)),
]

