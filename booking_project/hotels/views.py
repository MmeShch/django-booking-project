from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels/hotel_list.html'
    context_object_name = 'hotels'
    paginate_by = 5

    def get_queryset(self):
        return Hotel.objects.filter(deleted=False).select_related('rooms')


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/hotel_detail.html'
    context_object_name = 'hotel'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Hotel.objects.filter(deleted=False).prefetch_related('rooms__photos', 'photos', 'reviews')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.object.rooms.filter(deleted=False)
        return context


class RoomDetailView(DetailView):
    model = Room
    template_name = 'hotels/room_detail.html'
    context_object_name = 'room'

    def get_queryset(self):
        return Room.objects.filter(deleted=False).select_related('hotel')


#------------------API---------------------------------------
class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.filter(deleted=False).select_related('rooms')
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.filter(deleted=False).select_related('hotel')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['hotel_id'] = self.kwargs.get('hotel_pk')
        return context

