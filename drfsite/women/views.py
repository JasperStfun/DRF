from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action


from .models import *
from .serializers import *


class WomenViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


