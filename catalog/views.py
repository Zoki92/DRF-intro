from django.http import HttpResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content as JSON
#     """

#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)


# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return JSONResponse(serializer.data)


# class ProductList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)


# class ProductDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product,
#                                        data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            product_id=self.kwargs['pk']
        )


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        review = self.kwargs['review_id']
        return Review.objects.filter(id=review)
