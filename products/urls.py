from django.urls import path
from .views import *

urlpatterns = [
 
    path('',main_menu_page, name='main_menu_url'),
    path('shops/',shop_list, name='shop_list_url'),
    path('products/',product_list, name='product_list_url'),
    path('products_sort_price/',product_list_sort_price, name='product_list_sort_price_url'),
    path('products_select_price/',ProductSelectPriceView.as_view(), name='product_select_price_url'),
    path('products_search/',ProductSearchView.as_view(), name='product_search_url'),
    path('products_active/',product_list_active, name='product_list_active_url'),
    path('categories/',category_list, name='category_list_url'),
##    path('voting/',voting_list, name='voting_list_url'),
##    path('voting/create/',VotingCreate.as_view(), name='voting_create_url'),
    path('shops/<int:pk>/',ShopDetailView.as_view(), name='shop_detail_url'),
    path('products/<int:pk>/',ProductDetailView.as_view(), name='product_detail_url'),
    path('categories/<int:pk>/',CategoryDetailView.as_view(), name='category_detail_url'),
    path('categories/create/',CategoryCreateView.as_view(), name='category_create_url'),
    path('products/create/',ProductCreateView.as_view(), name='product_create_url'),
    path('shops/create/',ShopCreateView.as_view(), name='shop_create_url'),
    path('shops/update/<int:pk>/',ShopUpdateView.as_view(), name='shop_update_url'),
    path('product/update/<int:pk>/',ProductUpdateView.as_view(), name='product_update_url'),



##    path('voting/<int:pk>/',VotingDetail.as_view(), name='voting_detail_url'),  
##         
    
]
