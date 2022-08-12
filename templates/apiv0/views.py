from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from website.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
# Create your views here.
























def test_api_view(request):
    first_Technique = Technique.objects.first()
    f_b = {
        'name': first_Technique.name,
        'Company':first_Technique.company.title,
        'price': first_Technique.price,
    }
    return JsonResponse(f_b)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Technique_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=TechniqueSerializer(instance=Technique.objects.all(), many=True).data, status=200)
        else:
            the_Technique = get_object_or_404(Technique, pk=pk)
            return Response(data=TechniqueSerializer(instance=the_Technique).data, status=200)
    
    elif request.method == "POST":
        sb = TechniqueSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Technique = get_object_or_404(Technique, pk=pk)
        sb = TechniqueSerializer(data=request.data, instance=the_Technique)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Technique = get_object_or_404(Technique, pk=pk)
        the_Technique.delete()
        return Response('Deleted', status=200)


class TechniqueListAPIView(ListAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer


class TechniqueCreateAPIView(CreateAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer


class TechniqueUpdateAPIView(UpdateAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer


class TechniqueDestroyAPIView(DestroyAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer





@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Brand_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=BrandSerializer(instance=Brand.objects.all(), many=True).data, status=200)
        else:
            the_Brand = get_object_or_404(Brand, pk=pk)
            return Response(data=BrandSerializer(instance=the_Brand).data, status=200)
    
    elif request.method == "POST":
        sb = BrandSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Brand = get_object_or_404(Brand, pk=pk)
        sb = BrandSerializer(data=request.data, instance=the_Brand)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Brand = get_object_or_404(Brand, pk=pk)
        the_Brand.delete()
        return Response('Deleted', status=200)


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDestroyAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Size_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=SizeSerializer(instance=Size.objects.all(), many=True).data, status=200)
        else:
            the_Size = get_object_or_404(Size, pk=pk)
            return Response(data=SizeSerializer(instance=the_Size).data, status=200)
    
    elif request.method == "POST":
        sb = SizeSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Size = get_object_or_404(Size, pk=pk)
        sb = SizeSerializer(data=request.data, instance=the_Size)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Size = get_object_or_404(Size, pk=pk)
        the_Size.delete()
        return Response('Deleted', status=200)


class SizeListAPIView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class SizeUpdateAPIView(UpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class SizeDestroyAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer







@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Company_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CompanySerializer(instance=Company.objects.all(), many=True).data, status=200)
        else:
            the_Company = get_object_or_404(Company, pk=pk)
            return Response(data=CompanySerializer(instance=the_Company).data, status=200)
    
    elif request.method == "POST":
        sb = CompanySerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Company = get_object_or_404(Company, pk=pk)
        sb = CompanySerializer(data=request.data, instance=the_Company)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Company = get_object_or_404(Company, pk=pk)
        the_Company.delete()
        return Response('Deleted', status=200)


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDestroyAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class AksiyaListAPIView(ListAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer


class AksiyaCreateAPIView(CreateAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer


class AksiyaUpdateAPIView(UpdateAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer


class AksiyaDestroyAPIView(DestroyAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer



@api_view(['GET', 'POST', 'PUT', 'DELETE'])

def Aksiya_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=AksiyaSerializer(instance=Aksiya.objects.all(), many=True).data, status=200)
        else:
            the_Aksiya = get_object_or_404(Aksiya, pk=pk)
            return Response(data=AksiyaSerializer(instance=the_Aksiya).data, status=200)
    
    elif request.method == "POST":
        sb = AksiyaSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Aksiya = get_object_or_404(Aksiya, pk=pk)
        sb = AksiyaSerializer(data=request.data, instance=the_Aksiya)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Aksiya = get_object_or_404(Aksiya, pk=pk)
        the_Aksiya.delete()
        return Response('Deleted', status=200)

