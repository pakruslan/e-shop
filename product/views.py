from django.forms import models
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions as p, viewsets, generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from django.contrib import messages

from .models import Product, Category, Comment
from .serializers import ProductSerializer, CategorySerializer, CreateUpdateProductSerializer, CommentSerializer
from .filters import ProductFilter


class MyPagination(PageNumberPagination):
    page_size = 1


class CategoriesList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProductSerializer
        return CreateUpdateProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retreiver', 'search']:
            permissions = [p.AllowAny]
        else:
            permissions = [p.IsAdminUser]
        return [permissions() for permissions in permissions]

    @action(methods=['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        if q is not None:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [p.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
# class AddComment(models.ModelForm):
#     def addcomment(self,id):
#         url = request.META.get('HTTP_REFERER')  # get last url
#             # return HttpResponse(url)
#         if request.method == 'POST':  # check post
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 data = Comment()  # create relation with model
#                 data.comment = form.cleaned_data['comment']
#                 data.rate = form.cleaned_data['rate']
#                 data.ip = request.META.get('REMOTE_ADDR')
#                 data.product_id = id
#                 current_user = request.user
#                 data.user_id = current_user.id
#                 data.save()  # save data to table
#                 messages.success(request, "Your review has ben sent. Thank you for your interest.")
#                 return HttpResponseRedirect(url)
#
#             return HttpResponseRedirect(url)