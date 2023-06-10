from django.urls import path

from smarttender.views import ProductListView, update_tender, get_cell_data, EnsTruListView
from smarttender.views.mnn_products import find_similar_products, similar_products, selected_product
from smarttender.views.tenders import TenderListView, tender_graphql_view, tender_save_view

urlpatterns = [
    path('', TenderListView.as_view(), name='index'),
    path('parse_tenders', tender_graphql_view, name='tender_graphql_view'),
    path('save_tenders', tender_save_view, name='tender_save_view'),
    path('enstru_codes', EnsTruListView.as_view(), name='enstru_list_view'),
    path('products', ProductListView.as_view(), name='product_list'),
    path('update_tender/', update_tender, name='update_tender'),
    path('find_similar_products/<int:tender_id>/', find_similar_products, name='find_similar_products'),
    path('similar_products/<int:tender_id>/', similar_products, name='similar_products'),
    path('selected_product/', selected_product, name='selected_product'),
    path('get_cell_data/', get_cell_data, name='get_cell_data'),
]
