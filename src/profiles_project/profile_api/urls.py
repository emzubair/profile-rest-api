from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

myRouter = DefaultRouter()
myRouter.register('myViewSet',views.HelloViewSets,base_name='custom')
myRouter.register('profile',views.UserProfileViewSet)

urlpatterns = [
    url(r'^hello-view/',views.HelloAPIView.as_view()),
    url(r'',include(myRouter.urls))
]
