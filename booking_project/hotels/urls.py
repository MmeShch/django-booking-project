from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.HotelListView.as_view(), name='hotel_list'),
    path('<slug:slug>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path('room/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
]

router = DefaultRouter()
router.register(r'api/hotels', views.HotelViewSet)
router.register(r'api/rooms', views.RoomViewSet)

urlpatterns += router.urls