from rest_framework import serializers
from .models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    sub_category = CategorySerializer3(many=True)  # 通过二级分类获取三级分类

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sub_category = CategorySerializer2(many=True)  # 通过一级分类获取到二级分类，由于一级分类下有多个二级分类，需要设置many=True

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # 自定义字段覆盖原有的字段，实例化

    class Meta:
        model = Goods
        fields = '__all__'


# 获取父级分类
class ParentCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class ParentCategorySerializer2(serializers.ModelSerializer):
    parent_category = ParentCategorySerializer3()

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class ParentCategorySerializer(serializers.ModelSerializer):
    parent_category = ParentCategorySerializer2()

    class Meta:
        model = GoodsCategory
        fields = '__all__'
