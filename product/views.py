from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions , viewsets
from rest_framework.response import Response


from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, CreateUpdateProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return Response(serializers.data)


class ProductsList(APIView): #View 
    
    def get(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)



class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProduct(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class =  CreateUpdateProductSerializer


class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    permissions_classes = [permissions.IsAdminUser]
    serializer_class = CreateUpdateProductSerializer


class DeleteProduct(DestroyAPIView):
    queryset = Product.objects.all()
    permissions_classes = [permissions.IsAdminUser]



class CategoriesList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list' or self.action == 'retrieve':
#             return ProductSerializer
#         return CreateUpdateProductSerializer

    # def get_permissions(self):
    #     # if self.action == 'list' or self.action == 'retrieve':
    #     if self.action in ['list', 'retreiver']:
    #         permissions = [p.AllowAny]
    #     else:
    #         permissions = [p.IsAdminUser]
    #     return [permissions() for permissions in permissions]