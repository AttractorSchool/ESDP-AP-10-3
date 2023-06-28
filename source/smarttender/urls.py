from django.urls import path

from smarttender.views import ProductListView, update_tender, get_cell_data
from smarttender.views.enstru_codes import EnsTruListView, enstru_create_view
from smarttender.views.mnn_products import find_similar_products, similar_products, selected_product
from smarttender.views.tenders import TenderListView, tender_graphql_view, tender_save_view
from smarttender.views.price_pdf import pdf_view,opt_pdf_price

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
    path('enstru_create', enstru_create_view, name='enstru_create_view'),
    path('pdf_upload', pdf_view, name='pdf_view'),
    path('opt_pdf_upload', opt_pdf_price, name='opt_pdf_view'),

]
