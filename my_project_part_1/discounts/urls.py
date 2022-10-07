# TODO настраиваем urls здесь
from django.urls import path

from my_project_part_1.discounts.views import DiscountListView, DiscountDetailView

urlpatterns = [
    path('discount/', DiscountListView.as_view()),
    path('discount/<int:pk>', DiscountDetailView.as_view()),

]
