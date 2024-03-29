
from rest_framework import serializers
from ..models import Category,Product,ProductImage,Newsletter,Basket,Order,OrderItem,ShippingInfo,BillingInfo,PaymentInfo,Wishlist,ProductComment,ProductRating
from django.contrib.auth import get_user_model
from django.db.models import F, FloatField,Value,Avg
from django.db.models.functions import Coalesce

User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name","surname")




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("parent","name","id","icon")

    def to_representation(self, instance):
        repr_= super().to_representation(instance)
        qs = Category.objects.filter(parent=instance)
        if qs.exists():
            repr_['children']=CategorySerializer(qs,many=True).data

        return repr_



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating

        fields = "__all__"
        extra_kwargs = {
            "user":{
                "read_only":True
            },
            "product":{
                "read_only":True
            }
        }

    

from django.utils.translation import gettext_lazy as _
from services.choices import SKINTYPE,STATUS

class ProductListSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    discount_percent = serializers.IntegerField(read_only=True)
    rating = serializers.SerializerMethodField(read_only=True)
    skin = serializers.CharField(source='get_skin_display')
    status = serializers.CharField(source='get_status_display')


    class Meta:
        model = Product
        fields = ("name", "price", "total_price", "discount_percent", "category", "status", "id","skin","rating")

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_['category'] = CategorySerializer(instance.category).data
        repr_['images'] = ImageSerializer(instance.productimage_set.first()).data

        # if instance.discount_percent == 0:
        #     repr_.pop("discount_percent")

        # if not instance.status:
        #     repr_.pop("status")

        return repr_
    

    def get_rating(self,obj):
        ratings = ProductRating.objects.filter(product=obj.id).aggregate(Avg('rating'))['rating__avg']

        return ratings
    
    def get_skin_display(self, obj):
        return _(dict(SKINTYPE).get(obj.skin))
 

    def get_status_display(self, obj):
        return _(dict(STATUS).get(obj.status))
    


class NewsletterSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ("email",)

    def validate(self, attrs):
        email = attrs.get("email")
        if Newsletter.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error":"You are already subscribed."})
        
        return attrs
    
    def create(self, validated_data):
        email = validated_data.get("email")
        subscriber = Newsletter(email=email)
        subscriber.save()
        
        return subscriber
    

    
class RelatedProductSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    discount_percent = serializers.IntegerField(read_only=True)
    rating = serializers.SerializerMethodField(read_only=True)
    skin = serializers.CharField(source='get_skin_display')
    status = serializers.CharField(source='get_status_display')


    class Meta:
        model = Product
        fields = ("id", "title", "price", "total_price", "status", "discount_percent","skin","rating")

    def to_representation(self, instance):
        annotated_instance = Product.objects.annotate(
            discount_price=Coalesce('discount', Value(0), output_field=FloatField()),
            discount_percent=F("discount_price") * 100 / F("price")
        ).get(id=instance.id)

        repr_ = super().to_representation(annotated_instance)

        repr_['category'] = CategorySerializer(annotated_instance.category).data
        repr_['images'] = ImageSerializer(annotated_instance.productimage_set.first()).data

        if annotated_instance.discount_percent == 0:
            repr_.pop("discount_percent")

        if not annotated_instance.status:
            repr_.pop("status")

        return repr_
    
    def get_rating(self,obj):
        ratings = ProductRating.objects.filter(product=obj.id).aggregate(Avg('rating'))['rating__avg']

        return ratings

    def get_skin_display(self, obj):
        return _(dict(SKINTYPE).get(obj.skin))
 

    def get_status_display(self, obj):
        return _(dict(STATUS).get(obj.status))
    


class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    discount_percent = serializers.IntegerField(read_only=True)
    related_products = RelatedProductSerializer(many=True, read_only=True)  
    rating = serializers.SerializerMethodField(read_only=True)
    skin = serializers.CharField(source='get_skin_display')
    status = serializers.CharField(source='get_status_display')


    class Meta:
        model = Product
        fields = ("id", "title", "price", "total_price", "status", "discount_percent","skin","rating","code","related_products","sku")
    
    def to_representation(self, instance):
        repr_= super().to_representation(instance)
        repr_['category']=CategorySerializer(instance.category).data
        repr_['images']=ImageSerializer(instance.productimage_set.all(),many=True).data


        if not instance.status:
            repr_.pop("status")

        if not instance.code:
            repr_.pop("code")

        # repr_["slug"] = instance.slug
        
        related_products = Product.objects.filter(category=instance.category).exclude(id=instance.id)[:5]
        repr_['related_products'] = RelatedProductSerializer(related_products, many=True).data

        return repr_       
    
    def get_rating(self,obj):
        ratings = ProductRating.objects.filter(product=obj.id).aggregate(Avg('rating'))['rating__avg']

        return ratings

    def get_skin_display(self, obj):
        return _(dict(SKINTYPE).get(obj.skin))
 

    def get_status_display(self, obj):
        return _(dict(STATUS).get(obj.status))
    



class WishlistSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    product_title = serializers.SerializerMethodField()
    price = serializers.FloatField(source='products.price',read_only=True)
    status = serializers.CharField(source="products.status",read_only=True)

    class Meta:
        model = Wishlist
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "session_key": {"read_only": True},
            "products": {"read_only": True},

        }


    def get_product_image(self, obj):
        try:
            product_images = ProductImage.objects.filter(product=obj.products)
            if product_images.exists():
                product_image = product_images.first()
                return ImageSerializer(product_image).data.get('image')
            else:
                return None
        except ProductImage.DoesNotExist:
            return None

        
    def get_total_price(self, obj):
        product_price = obj.products.price or 0 
        product_discount = obj.products.discount or 0
        return product_price - product_discount


    def get_product_title(self,obj):
        return obj.products.title



class BasketSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    product_title = serializers.SerializerMethodField()
    price = serializers.FloatField(source='product.price',read_only=True)


    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'price', 'total_price', 'product_image','product_title')

        extra_kwargs = {
            "product":{"read_only":True}
        }

    def get_product_image(self, obj):
        try:
            product_images = ProductImage.objects.filter(product=obj.product)
            if product_images.exists():
                product_image = product_images.first()
                return ImageSerializer(product_image).data.get('image')
            else:
                return None
        except ProductImage.DoesNotExist:
            return None


    def get_product_title(self,obj):
        return obj.product.title
    
    def get_total_price(self, obj):
        product_price = obj.product.price or 0  # Use 0 if product price is None
        product_discount = obj.product.discount or 0  # Use 0 if product discount is None
        return product_price - product_discount


class BasketItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    product_title = serializers.SerializerMethodField()
    price = serializers.FloatField(source='product.price')

    class Meta:
        model = Basket
        fields = ('id', 'product', 'price', 'total_price', 'product_image','product_title')

    def get_product_image(self, obj):
        try:
            product_images = ProductImage.objects.filter(product=obj.product)
            if product_images.exists():
                product_image = product_images.first()
                return ImageSerializer(product_image).data.get('image')
            else:
                return None
        except ProductImage.DoesNotExist:
            return None
        
    def get_total_price(self, obj):
        product_price = obj.product.price or 0  # Use 0 if product price is None
        product_discount = obj.product.discount or 0  # Use 0 if product discount is None
        return product_price - product_discount


    def get_product_title(self,obj):
        return obj.product.title





class  RemoveCartItemSerializer(serializers.Serializer):
    class Meta:
        model=Basket
        fields = ('product',)
        extra_kwargs={
            "product":{"read_only":True}
        }


class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInfo
        fields = "__all__"
        extra_kwargs={
            "user":{"read_only":True},
            }

class BillingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInfo
        fields = '__all__'
        extra_kwargs={
            "user":{"read_only":True},
            }


class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = '__all__'
        extra_kwargs={
            "user":{"read_only":True},
            "order":{"read_only":True},
            }


        
class PlaceOrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'



class OrderListSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        exclude = ("payment_info","shipping_info","billing_info","session_key")


    def get_total_price(self, obj):
        total_price = sum([item.product.price * item.quantity for item in obj.items.all()])
        return total_price
    



    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "product": {"read_only": True},
            "session_key": {"read_only": True},
            "email":{"read_only":True},
        }
    
    def to_representation(self, instance):
        repr_ = super().to_representation(instance)

        children = CommentSerializer(
            ProductComment.objects.filter(parent=instance),
            many=True
        ).data

        if children:
            repr_['children'] = children

        return repr_



class CommentUpdateSerializer(serializers.ModelSerializer):
    # comment = serializers.CharField(required=False)

    class Meta:
        model = ProductComment
        fields = ("comment","user")
        extra_kwargs={"user":{"read_only":True},}


    def validate(self, attrs):
        email = attrs.get("email")
        comment=attrs.get("comment")

        check_comment = ProductComment.objects.filter(email=email,comment=comment)

        if not check_comment:
            raise serializers.ValidationError({"error":"This is not your comment"})

        return attrs

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    


class LanguageSerializer(serializers.Serializer):
    language = serializers.CharField()