from django.urls import path
from smarttender.views import TenderListView, ProductListView, update_tender, TenderAPIListView, get_cell_data


urlpatterns = [
    path('', TenderListView.as_view(), name='index'),
    path('products', ProductListView.as_view(), name='product_list'),
    path('update_tender/', update_tender, name='update_tender'),
    path('tenders', TenderAPIListView.as_view(), name='tender_api_list'),
    path('get_cell_data/', get_cell_data, name='get_cell_data'),
]
