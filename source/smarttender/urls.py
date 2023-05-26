from django.urls import path

from smarttender.views import TenderListView, ProductListView, update_tender

urlpatterns = [
    path('', TenderListView.as_view(), name='index'),
    path('', ProductListView.as_view(), name='index'),
    path('update_tender/', update_tender, name='update_tender'),
]
