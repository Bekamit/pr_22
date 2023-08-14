from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import RegisterView, LoginView, UserListView, RegistrationPhoneView, VerifyEmail, UserViewSet
from hotel.views import BookingViewSet, EquipmentViewSet, HotelViewSet, CommentViewSet
from restourant.views import ProductViewSet, CategoryViewSet, LikeCreateView
from services_pr.views import ServicesViewSet, SelectViewSet, UnderViewSet, BookingUnderServicesViewSet

router = routers.DefaultRouter()
router.register('bookings', BookingViewSet)
router.register('equipments', EquipmentViewSet)
router.register('hotels', HotelViewSet)
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)
router.register('services', ServicesViewSet)
router.register('select_services', SelectViewSet)
router.register('under_service', UnderViewSet)

router.register('booking-services', BookingUnderServicesViewSet)

router.register('product', ProductViewSet)
router.register('category_restourant', CategoryViewSet)
router.register('likes', LikeCreateView)

urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('register-phone/', RegistrationPhoneView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('bookings/', UserListView.as_view()),
    path('', include(router.urls)),
]






