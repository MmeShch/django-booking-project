from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .models import Hotel, Room

class HotelListView(ListView):
    model = Hotel
    paginate_by = 5

    def get_queryset(self):
        return Hotel.objects.filter(deleted=False).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_authenticated'] = self.request.user.is_authenticated
        return context


class HotelDetailView(DetailView):
    model = Hotel

    def get_queryset(self):
        return Hotel.objects.filter(deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_authenticated'] = self.request.user.is_authenticated
        context['rooms'] = self.object.rooms.filter(deleted=False)
        return context


class RoomDetailView(DetailView):
    model = Room

    def get_queryset(self):
        return Room.objects.filter(deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_authenticated'] = self.request.user.is_authenticated
        context['room_free'] = self.object.available
        return context


class AdminHotelListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Hotel

    def test_func(self):
        return self.request.user.is_staff


class AdminHotelCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Hotel
    fields = ['name', 'location', 'description', 'photos', 'rating']

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, 'Hotel is created!')
        return super().form_valid(form)

    def get_success_url(self):
        return 'hotels:admin_hotel_list'