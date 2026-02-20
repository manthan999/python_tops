from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from myapp.models import *
from myapp.serializer import *
from rest_framework.permissions import AllowAny,IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [IsAdminUser]

        # GET USER BY ID -> anyone allowed
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]

        # CREATE USER -> login required
        elif self.action == 'create':
            permission_classes = [AllowAny]

        # UPDATE USER -> admin only
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]

        # PARTIAL UPDATE -> admin only
        elif self.action == 'partial_update':
            permission_classes = [IsAuthenticated]

        # DELETE USER -> admin only
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {
                "status": True,
                "message": "User deleted successfully"
            },
            status=status.HTTP_200_OK
        )

class CategoryViewSet(ModelViewSet):

    queryset =Category.objects.all()
    serializer_class = CategorySerializer



    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [AllowAny]

       
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]

     
        elif self.action == 'create':
            permission_classes = [IsAdminUser]

        
        elif self.action == 'update':
            permission_classes = [IsAdminUser]

        elif self.action == 'partial_update':
            permission_classes = [IsAdminUser]

       
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]

        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {
                "status": True,
                "message": "Category deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    

class ProductViewSet(ModelViewSet):

    queryset =Product.objects.all()
    serializer_class = ProductSerializer



    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [AllowAny]

       
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]

     
        elif self.action == 'create':
            permission_classes = [AllowAny]

        
        elif self.action == 'update':
            permission_classes = [AllowAny]

        elif self.action == 'partial_update':
            permission_classes = [AllowAny]

       
        elif self.action == 'destroy':
            permission_classes = [AllowAny]
        
        elif self.action =='products_by_category':
            permission_classes = [AllowAny]

        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {
                "status": True,
                "message": "Product deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>[^/.]+)')
    def products_by_category(self, request, category_id=None):

        products = Product.objects.filter(category_id=category_id)

        if not products.exists():
            return Response({
                "status": False,
                "message": "No products found in this category"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(products, many=True)

        return Response({
            "status": True,
            "category_id": category_id,
            "total_products": products.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)



class CartViewSet(ModelViewSet):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_cart(self, user):
        cart, created = Cart.objects.get_or_create(user=user)
        return cart
    
    def list(self, request):
        cart = self.get_cart(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    
    @action(detail=False, methods=['post'],serializer_class=CartItemSerializer)
    def add(self, request):

        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=404)

        cart = self.get_cart(request.user)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity

        item.save()

        return Response({
            "status": True,
            "message": "Product added to cart"
        }, status=status.HTTP_200_OK)
    

    def list(self, request):
        cart = self.get_cart(request.user) 
        serializer = CartSerializer(cart)   
        return Response(serializer.data)
    

    @action(detail=False, methods=['delete']) 
    def remove(self, request): 
        cart = self.get_cart(request.user) 
        product_id = request.data.get('product_id') 
        item = get_object_or_404(CartItem, cart=cart, product_id=product_id) 
        item.delete() 
        return Response({"message": "Item removed"})
    


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)