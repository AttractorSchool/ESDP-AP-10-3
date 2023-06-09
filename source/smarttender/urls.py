from django.urls import path
from smarttender.views import TenderListView, ProductListView, update_tender, TenderAPIListView, get_cell_data

from smarttender.views.mnn_products import find_similar_products, similar_products, selected_product

urlpatterns = [
    path('', TenderListView.as_view(), name='index'),
    path('products', ProductListView.as_view(), name='product_list'),
    path('update_tender/', update_tender, name='update_tender'),
    path('tenders', TenderAPIListView.as_view(), name='tender_api_list'),
    path('find_similar_products/<int:tender_id>/', find_similar_products, name='find_similar_products'),
    path('similar_products/<int:tender_id>/', similar_products, name='similar_products'),
    path('selected_product/', selected_product, name='selected_product'),
    path('get_cell_data/', get_cell_data, name='get_cell_data'),
]