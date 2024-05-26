from django.shortcuts import render
from .serializers import CategorSignsSerializer, RoadSignsSerializer
from .models import CategorySigns, RoadSings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ListCategoryApiView(APIView):
    def get(self, request):
        category = CategorySigns.objects.all()
        serializer = CategorSignsSerializer(category, many=True)
        serializer_data = {
            'cateory': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class ListRoadSignsApiView(APIView):
    def get(self, request):
        model = RoadSings.objects.all()
        serializer = RoadSignsSerializer(model, many=True)
        serializer_data = {
            'data': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class DetailRoadSignsApiView(APIView):
    def get(self, request, pk):
        model = RoadSings.objects.get(id=pk)
        serializer = RoadSignsSerializer(model)
        serializer_data = {
            'data': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)