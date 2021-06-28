from rest_framework import serializers
from accounts.models import User
from doshop.models import Category, Company, Product
from orders.models import Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta :
        model = Company
        fields = ('name',)


class specialPriceProductsSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    class Meta :
        model = Product
        fields = ('name', 'company', 'specialـprice')


class ProductsOFCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)
    """
    def validate(self, data):
        if data['name'] == 'laptop' :
            raise serializers.ValidationError({"error":"mobile is not here"})
        return data
    """


    
