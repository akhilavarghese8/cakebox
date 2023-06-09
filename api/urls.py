from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("register",views.UserView,basename="users"),
router.register("cakes",views.CakeView,basename="cake"),
router.register("carts",views.CartListView,basename="cartlist"),
router.register("reviews",views.ReviewListView,basename="reviewlist")




urlpatterns = [
    path("token/",ObtainAuthToken.as_view()),
    

]+router.urls
