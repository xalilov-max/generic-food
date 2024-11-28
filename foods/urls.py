from django.urls import path
from .views import FoodListView, FoodDetailView, FoodCreateView, FoodUpdateView, FoodDeleteView

urlpatterns = [
    path('', FoodListView.as_view(), name='food_list'),
    path('<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('create/', FoodCreateView.as_view(), name='food_create'),
    path('<int:pk>/update/', FoodUpdateView.as_view(), name='food_update'),
    path('<int:pk>/delete/', FoodDeleteView.as_view(), name='food_delete'),
]
