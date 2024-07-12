# product/serializers.py
from rest_framework import serializers
from .models import Category, Subcategory, Product, ProductImage, Coupon

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('name',)

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ( 'title', 'description', 'price', 'discount', 'bestseller', 'category', 'subcategory', 'added_by', 'created_at', 'images')
        
        def create(self, validated_data):
            images_data = self.context.get('request').FILES
            product_images = [ProductImage.objects.create(image=image) for image in images_data.getlist('images')]
        
            validated_data.pop('images', None)
            product = Product.objects.create(**validated_data)
            for img in product_images:
                product.images.add(img)
                return product

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('discount', 'valid_from', 'valid_to', 'active')
