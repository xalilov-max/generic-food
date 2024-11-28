from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Food

class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'
    context_object_name = 'foods'
    ordering = ['-id']

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        if query:
            object_list = object_list.filter(nomi__icontains=query)
        return object_list

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'

class FoodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Food
    fields = ['food_type', 'nomi', 'tarkibi', 'narxi']
    template_name = 'food_form.html'
    success_url = reverse_lazy('food_list')
    permission_required = 'foods.add_food'

class FoodUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Food
    fields = ['food_type', 'nomi', 'tarkibi', 'narxi']
    template_name = 'food_form.html'
    success_url = reverse_lazy('food_list')
    permission_required = 'foods.change_food'

class FoodDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Food
    template_name = 'food_confirm_delete.html'
    success_url = reverse_lazy('food_list')
    permission_required = 'foods.delete_food'
