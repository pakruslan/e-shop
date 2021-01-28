from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import CategoriesList,CreateProduct,UpdateProduct,DeleteProduct,ProductDetail,ProductsList
from .views import ProductViewSet, CategoriesList,CommentCreate


router = DefaultRouter()
router.register('',ProductViewSet)

# products = ProductViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'post': 'create',
#     'delete': 'destroy',
#     'get': 'retrieve'
# })

urlpatterns = [
    # path('', ProductsList.as_view()),
    # path('detail/<str:pk>/',ProductDetail.as_view()),
    path('categories/', CategoriesList.as_view()),
    # path('categories/',CategoriesList.as_view()),
    # path('create/',CreateProduct.as_view()),
    # path('update/<str:pk>/',UpdateProduct.as_view()),
    # path('delete/<str:pk>/',DeleteProduct.as_view()),
    # path('',products),
    # path('<str:pk>/',products),class UpdateProduct(UpdateAPIView):
    #     queryset = Product.objects.all()
    #     permissions_classes = [permissions.IsAdminUser]
    #     serializer_class = CreateUpdateProductSerializer
    path('', include(router.urls)),
    # path('addcomment/<int:id>',AddComment.as_view(), name='addcomment'),

    #
    #
    # class DeleteProduct(DestroyAPIView):
    #     queryset = Product.objects.all()
    #     permissions_classes = [permissions.IsAdminUser]
    # path('',include(router.urls)),



    
]