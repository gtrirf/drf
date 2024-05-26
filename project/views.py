from django.shortcuts import render
from .serializers import CategorySignsSerializer, RoadSignsSerializer
from .models import CategorySigns, RoadSigns
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListCategoryApiView(APIView):
    def get(self, request):
        categories = CategorySigns.objects.all()
        serializer = CategorySignsSerializer(categories, many=True)
        serializer_data = {
            'category': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class ListRoadSignsApiView(APIView):
    def get(self, request):
        road_signs = RoadSigns.objects.all()
        serializer = RoadSignsSerializer(road_signs, many=True)
        serializer_data = {
            'data': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class DetailRoadSignsApiView(APIView):
    def get(self, request, pk):
        try:
            road_sign = RoadSigns.objects.get(id=pk)
        except RoadSigns.DoesNotExist:
            return Response({
                'error': 'RoadSign not found',
                'status': 'failure',
                'status_code': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = RoadSignsSerializer(road_sign)
        serializer_data = {
            'data': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)