
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('subcategories/', views.SubcategoryListCreate.as_view(), name='subcategory-list-create'),
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('coupons/', views.CouponListCreate.as_view(), name='coupon-list-create'),
    path('coupons/<int:pk>/', views.CouponDetail.as_view(), name='coupon-detail'),
]
